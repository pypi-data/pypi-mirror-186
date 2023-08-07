import os
import time
from typing import Callable, Tuple

import numpy as np
import tensorflow.keras as keras

from ..distance_prediction_model_base import DistanceBasePredictionModel
from .contrastive_model_description import tower_mlp, merge_constractive
from .....util.dataset import Dataset
from .....util.plotting import plot_history_df
from .....util.utils import contrastive_make_pairs


class ContrastiveKerasPredictionModel(DistanceBasePredictionModel):

    def __init__(self,
                 tower_model_description: Callable[[keras.layers.Input], keras.models.Model]
                 = tower_mlp,
                 merge_model_description: Callable[[keras.models.Model, keras.layers.Input,
                                                    keras.models.Model, keras.layers.Input],
                                                    keras.models.Model]
                 = merge_constractive,
                 output_dir: str = "keras_pred_model_out",
                 verbose=False,
                 nb_epochs=10,
                 batch_size: Callable[[int], int] = 16,
                 pair_function: Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]] =
                 contrastive_make_pairs):
        super().__init__(output_dir=output_dir, verbose=verbose)
        self.tower_model_description = tower_model_description
        self.merge_model_description = merge_model_description
        self.nb_epochs = 2000 if nb_epochs is None else nb_epochs
        assert isinstance(batch_size, Callable) or isinstance(batch_size, int)
        self.batch_size = batch_size
        self.callbacks = []
        self.model = None
        self.pair_function = pair_function

    def persist_model_trainables(self, path_like: str = 'saved_trainable_values', **kwargs):
        self.model.save_weights(os.path.join(self.output_dir, path_like))

    def restore_model_trainables(self,
                                 path_like: str,
                                 dataset: Dataset = None,
                                 pair_function: Callable[
                                     [np.ndarray, np.ndarray], Tuple[
                                         np.ndarray, np.ndarray]] = contrastive_make_pairs,
                                 **kwargs):
        pairs_train, labels_train = pair_function(dataset.trainset_data, dataset.trainset_labels)

        x_train_1 = pairs_train[:, 0]
        input_shape = x_train_1.shape[1:]

        self.model = self.build_model(input_shape)
        self.model.load_weights(path_like)

    def build_model(self, input_shape):
        input_layer = keras.layers.Input(input_shape)
        tower_1 = self.tower_model_description(input_layer)
        tower_2 = self.tower_model_description(input_layer)
        input_1 = keras.layers.Input(input_shape)
        input_2 = keras.layers.Input(input_shape)
        merge = self.merge_model_description(tower_1, input_1, tower_2, input_2)
        model_checkpoint = keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(self.output_dir, 'best_model.hdf5'),
            monitor='loss',
            save_best_only=True,
            save_weights_only=True)
        self.callbacks = [model_checkpoint]
        return merge

    def fit(self, dataset: Dataset):
        pairs_train, labels_train = self.pair_function(dataset.trainset_data, dataset.trainset_labels)

        # make validation pairs
        pairs_val, labels_val = self.pair_function(dataset.validationset_data, dataset.validationset_labels)

        # split trainig pairs
        x_train_1 = pairs_train[:, 0]
        x_train_2 = pairs_train[:, 1]

        # split validation pairs
        x_val_1 = pairs_val[:, 0]
        x_val_2 = pairs_val[:, 1]

        input_shape = x_train_1.shape[1:]

        y_train, y_val = labels_train, labels_val

        self.model = self.build_model(input_shape)
        self.model.build(input_shape=input_shape)
        if self.verbose:
            print(self.model.summary())

        self.persist_model_trainables('model_init.hdf5')

        if self.batch_size is Callable:
            batch_size = self.batch_size(x_train_1.shape[0])
        else:
            batch_size = self.batch_size

        start_time = time.time()
        hist = self.model.fit([x_train_1, x_train_2], y_train, batch_size=batch_size, epochs=self.nb_epochs,
                              verbose=self.verbose, validation_data=([x_val_1, x_val_2], y_val),
                              callbacks=self.callbacks)

        duration = time.time() - start_time
        plot_history_df(hist, self.output_dir)

        if self.verbose:
            print(f"Contrastive distance learning model fitted in {round(duration, 2)} seconds!")

        self.persist_model_trainables('last_model.hdf5')
        # Not using restore here to not build a new model
        self.model.load_weights(os.path.join(self.output_dir, 'best_model.hdf5'))

        keras.backend.clear_session()

    def predict(self, x_test_1, x_test_2):
        y_pred = self.model.predict([x_test_1, x_test_2])
        return y_pred
