import os
import time
from typing import Callable

import numpy as np
import tensorflow.keras as keras

from useckit.paradigms.time_series_classification.prediction_models.keras_model_descriptions import \
    dl4tsc_cnn_padding_valid
from .tsc_prediction_model_base import TSCBasePredictionModel
from ....util.dataset import Dataset
from ....util.utils import calculate_metrics, save_logs, save_test_duration


class ClassificationKerasPredictionModel(TSCBasePredictionModel):
    def persist_model_trainables(self, path_like: str = 'saved_trainable_values', **kwargs):
        self.model.save_weights(os.path.join(self.output_dir, path_like))

    def restore_model_trainables(self, path_like, dataset: Dataset = None, **kwargs):
        _, _, _, _, _, input_shape, nb_classes = self.convert_dataset_to_legacy_values(dataset)
        self.model = self.build_model(input_shape, nb_classes)
        self.model.load_weights(path_like)

    def __init__(self,
                 model_description: Callable[[keras.layers.Input, int], tuple[keras.models.Model, list[Callable]]]
                 = dl4tsc_cnn_padding_valid,
                 verbose: bool = True,
                 output_dir: str = "keras_model_out",
                 nb_epochs=2000,
                 class_weights=None,
                 batch_size: Callable[[int], int] = 16):
        super().__init__(output_dir=output_dir, verbose=verbose)
        self.model_description = model_description
        self.nb_epochs = 2000 if nb_epochs is None else nb_epochs
        self.class_weights = class_weights
        assert isinstance(batch_size, Callable) or isinstance(batch_size, int)
        self.batch_size = batch_size
        self.callbacks = []
        self.model = None

    def build_model(self, input_shape, nb_classes):
        input_layer = keras.layers.Input(input_shape)
        model, callbacks = self.model_description(input_layer, nb_classes)
        model_checkpoint = keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(self.output_dir, 'best_model.hdf5'),
            monitor='val_loss',
            save_best_only=True,
            save_weights_only=True)
        self.callbacks = [model_checkpoint]
        self.callbacks += callbacks
        return model

    def prepare_input(self, x):
        return x

    def fit(self, dataset: Dataset, *args, **kwargs):
        x_train, x_val, y_train, y_val, y_true, input_shape, nb_classes = self.convert_dataset_to_legacy_values(dataset)
        x_train = self.prepare_input(x_train)
        x_val = self.prepare_input(x_val)

        self.model = self.build_model(input_shape, nb_classes)
        if self.verbose:
            self.model.summary()

        self.persist_model_trainables('model_init.hdf5')

        if callable(self.batch_size):
            batch_size = self.batch_size(x_train.shape[0])
        else:
            batch_size = self.batch_size

        start_time = time.time()
        hist = self.model.fit(x_train, y_train, batch_size=batch_size, epochs=self.nb_epochs,
                              class_weight=self.class_weights,
                              verbose=self.verbose, validation_data=(x_val, y_val), callbacks=self.callbacks)
        duration = time.time() - start_time
        self._plot_history(hist)

        self.persist_model_trainables('last_model.hdf5')
        # Not using restore here to not build a new model
        self.model.load_weights(os.path.join(self.output_dir, 'best_model.hdf5'))

        y_pred = self.model.predict(x_val)
        # convert the predicted from binary to integer
        y_pred = np.argmax(y_pred, axis=1)

        save_logs(self.output_dir, hist, y_pred, y_true, duration, lr=False)
        keras.backend.clear_session()

    def predict(self, x_test, y_true, x_train, y_train, y_test, return_df_metrics=True):
        x_test = self.prepare_input(x_test)
        x_train = self.prepare_input(x_train)

        start_time = time.time()
        y_pred = self.model.predict(x_test)
        if return_df_metrics:
            y_pred = np.argmax(y_pred, axis=1)
            df_metrics = calculate_metrics(y_true, y_pred, 0.0)
            return df_metrics
        else:
            test_duration = time.time() - start_time
            try:
                save_test_duration(os.path.join(self.output_dir, 'test_duration.csv'), test_duration)
            except PermissionError:
                print(
                    'PermissionError: Could not save test_duration.csv in Classifier_Keras due to lack of permission.')
            return np.argmax(y_pred, axis=1)
