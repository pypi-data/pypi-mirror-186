import os.path
import pickle
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import tensorflow.keras as keras

from .anomaly_prediction_model_base import AnomalyBasePredictionModel
from .keras_model_descriptions import BaseDescription, SequentialAutoEncoder
from ....util.dataset import Dataset
from ....util.plotting import plot_history_df


@dataclass
class _IndividualModel:
    keras_model: keras.Model
    training_max_mse_threshold: float
    path_like_individual_model_file_name: str


class AutoEncoderKerasPredictionModel(AnomalyBasePredictionModel):
    def persist_model_trainables(self, path_like: str = 'saved_trainable_values',
                                 overridden_individual_file_name: str = None, **kwargs):
        for i, model in enumerate(self.models):
            self._persist_individual_model(i, model, path_like, overridden_individual_file_name)

    def _persist_individual_model(self, index: int, model: _IndividualModel,
                                  path_like_individual_model_parent_dir: str,
                                  path_like_individual_model_file_name_override: str = None):
        if path_like_individual_model_file_name_override is None:
            file_name = model.path_like_individual_model_file_name
        else:
            file_name = path_like_individual_model_file_name_override
        output_dir = self.modify_output_dir_for_individual_model(index,
                                                                 base_output_dir=path_like_individual_model_parent_dir)
        model.keras_model.save_weights(os.path.join(output_dir, file_name))
        with open(os.path.join(output_dir, file_name + ".max_mse.pickle"), 'wb') as f:
            pickle.dump(model.training_max_mse_threshold, f)

    def restore_model_trainables(self,
                                 path_like: str,
                                 dataset: Dataset = None,
                                 path_like_individual_models_file_name: str = 'best_model.hdf5',
                                 **kwargs):
        x_train = dataset.trainset_data
        input_shape = x_train.shape[1:]
        nb_classes = dataset.train_classes()
        keras_models_built = self.build_model(input_shape, nb_classes)
        for i, keras_model in enumerate(keras_models_built):
            model = _IndividualModel(keras_model=keras_model, training_max_mse_threshold=0.,
                                     path_like_individual_model_file_name=path_like_individual_models_file_name)
            self._restore_individual_model(i, model, path_like)

    def _restore_individual_model(self, index: int, model: _IndividualModel,
                                  path_like_individual_model_parent_dir: str):
        output_dir = os.path.join(path_like_individual_model_parent_dir, f'auto_encoder_{index}')
        model.keras_model.load_weights(os.path.join(output_dir, model.path_like_individual_model_file_name))
        with open(os.path.join(output_dir, model.path_like_individual_model_file_name + ".max_mse.pickle"), 'rb') as f:
            model.training_max_mse_threshold = pickle.load(f)

    def __init__(self,
                 model_description: BaseDescription = SequentialAutoEncoder(),
                 verbose: bool = True,
                 output_dir: str = "keras_prediction_model_out",
                 nb_epochs=100):
        super().__init__(output_dir=output_dir, verbose=verbose)
        self.validation_test_data_confusion_warning_printed_once = False
        self.model_description = model_description
        self.nb_epochs = nb_epochs
        self.models = []

    def _get_mse(self, a: np.ndarray, b: np.ndarray):
        """Performs MSE calculation for a single value, returns only one value"""
        # from sklearn.metrics import mean_squared_error
        return np.sqrt(((a - b) ** 2).mean())

    def build_model(self, input_shape, nb_classes):
        result = []
        for i in range(nb_classes):
            result.append(self.model_description.build_model(input_shape))
        return result

    def modify_output_dir_for_individual_model(self, index: int, base_output_dir: str = None) -> str:
        if base_output_dir is None:
            base_output_dir = self.output_dir
        output_dir = os.path.join(base_output_dir, f'auto_encoder_{index}')
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        return output_dir

    def _predict_training_data_for_max_mse(self, model: _IndividualModel, train_data: np.ndarray):
        preds = model.keras_model.predict(train_data)
        mse_list = []
        assert len(preds) == len(train_data)
        for pred, x in zip(preds, train_data):
            mse_list.append(self._get_mse(pred, x))
        return max(mse_list)

    def fit(self, dataset: Dataset):
        x_train, y_train = dataset.trainset_data, dataset.trainset_labels
        x_val, y_val = dataset.validationset_data, dataset.validationset_labels
        input_shape = x_train.shape[1:]
        nb_classes = dataset.train_classes()

        assert nb_classes > 0
        keras_models_built = self.build_model(input_shape, nb_classes)
        for i, keras_model in enumerate(keras_models_built):
            # find the elements in the training data that belong to class `i`
            training_indexes = y_train == i
            x_train_model_i = x_train[training_indexes]

            validation_indexes = y_val == i
            x_val_model_i = x_val[validation_indexes]

            model = _IndividualModel(keras_model=keras_model, training_max_mse_threshold=0.,
                                     path_like_individual_model_file_name='best_model.hdf5')
            self._persist_individual_model(i, model, self.output_dir, 'model_init.hdf5')

            if self.verbose:
                print(f'useckit info: fitting AE {i + 1} of {nb_classes}')
                model.keras_model.summary()

            callbacks = []
            model_checkpoint = keras.callbacks.ModelCheckpoint(
                filepath=os.path.join(self.modify_output_dir_for_individual_model(i),
                                      model.path_like_individual_model_file_name),
                monitor='loss',
                save_best_only=True,
                save_weights_only=True)
            callbacks.append(model_checkpoint)
            callbacks += self.model_description.callbacks()

            history = model.keras_model.fit(
                x_train_model_i,
                x_train_model_i,
                validation_data=(x_val_model_i, x_val_model_i),
                verbose=self.verbose,
                epochs=self.nb_epochs,
                callbacks=callbacks,
            )

            plot_history_df(history, self.modify_output_dir_for_individual_model(i))

            model.training_max_mse_threshold = self._predict_training_data_for_max_mse(model, x_train_model_i)
            self._persist_individual_model(i, model, self.output_dir, 'last_model.hdf5')

            model.keras_model.load_weights(os.path.join(self.modify_output_dir_for_individual_model(i),
                                                        model.path_like_individual_model_file_name))
            model.training_max_mse_threshold = self._predict_training_data_for_max_mse(model, x_train_model_i)
            # this really just saves the mse and overwrites the weights with same values already in the file,
            # but whatever
            self._persist_individual_model(i, model, self.output_dir, 'best_model.hdf5')

            # store model in internal array
            self.models.append(model)

    def predict(self, x_test):
        result = []
        for i, model in enumerate(self.models):
            mse_list = []
            preds = model.keras_model.predict(x_test)
            for pred, x in zip(preds, x_test):
                mse_list.append(self._get_mse(pred, x))
            result.append(np.array(mse_list) / model.training_max_mse_threshold)
        return np.array(result)
