import os
import time
from typing import Callable, Tuple

import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import metrics
import tensorflow_addons as tfa

from useckit.paradigms.distance_learning.prediction_models.distance_prediction_model_base import \
    DistanceBasePredictionModel
from useckit.util.dataset import Dataset
from useckit.util.plotting import plot_history_df


class OnlineTripletKerasPredictionModel(DistanceBasePredictionModel):
    def __init__(self,
                 model_description: Callable[[keras.layers.Input], keras.models.Model]
                 = None,
                 loss_function: Callable = None,
                 output_dir: str = "keras_pred_model_out",
                 verbose=False,
                 nb_epochs=10,
                 batch_size: Callable[[int], int] = 16):
        super().__init__(output_dir=output_dir, verbose=verbose)
        self.model_description = model_description
        self.nb_epochs = 2000 if nb_epochs is None else nb_epochs
        assert isinstance(batch_size, Callable) or isinstance(batch_size, int)
        self.batch_size = batch_size
        self.callbacks = None
        self.model = None
        self.loss_tracker = metrics.Mean(name="loss")
        if loss_function is None:
            # default case
            self.loss_function = tfa.losses.TripletSemiHardLoss()
        else:
            self.loss_function = loss_function

    def persist_model_trainables(self, path_like: str = 'saved_trainable_values', **kwargs):
        self.model.save_weights(os.path.join(self.output_dir, path_like))

    def restore_model_trainables(self,
                                 path_like: str,
                                 dataset: Dataset = None):
        pairs_train, labels_train = dataset.trainset_data, dataset.trainset_labels

        x_train_1 = pairs_train[:, 0]
        input_shape = x_train_1.shape[1:]

        self.model = self.build_model(input_shape)
        self.model.load_weights(path_like)

    def build_model(self, input_shape):
        if self.model_description is not None:
            return self.model_description(input_shape)
        else:  # return default model
            return tf.keras.Sequential([
                tf.keras.layers.Dense(400, input_shape=input_shape, activation="tanh"),
                tf.keras.layers.Dense(300, activation="tanh"),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(256, activation=None),  # No activation on final dense layer
                tf.keras.layers.Lambda(lambda x: tf.math.l2_normalize(x, axis=1))  # L2 normalize embeddings
            ])

    def fit(self, dataset: Dataset):
        pairs_train, labels_train = dataset.trainset_data, dataset.trainset_labels

        # make validation pairs
        pairs_val, labels_val = dataset.validationset_data, dataset.validationset_labels
        y_train, y_val = labels_train, labels_val

        input_shape = pairs_train.shape[1:]

        self.model = self.build_model(input_shape=input_shape)

        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(0.001),
            loss=self.loss_function
        )

        self.model.build(input_shape=input_shape)

        if self.verbose:
            print(self.model.summary())

        self.persist_model_trainables('model_init.hdf5')

        batch_size = self.batch_size

        model_checkpoint = keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(self.output_dir, 'best_model.hdf5'),
            monitor='loss',
            save_best_only=True,
            save_weights_only=True)
        self.callbacks = [model_checkpoint]

        start_time = time.time()
        hist = self.model.fit(x=pairs_train, y=y_train, batch_size=batch_size, epochs=self.nb_epochs,
                              verbose=self.verbose, validation_data=tuple([pairs_val, y_val]),
                              callbacks=self.callbacks,
                              shuffle=True)  # shuffle is particularly important for these types of online losses

        duration = time.time() - start_time
        plot_history_df(hist, self.output_dir)

        if self.verbose:
            print(f"Tripple tower distance learning model fitted in {round(duration, 2)} seconds!")

        self.persist_model_trainables('last_model.hdf5')
        # Not using restore here to not build a new model
        self.model.load_weights(os.path.join(self.output_dir, 'best_model.hdf5'))

        keras.backend.clear_session()

    def predict(self, x_test_1, x_test_2, distance_function="euclidean"):
        """Returns a calculated distance between two input samples from the model's embedding space."""
        y_pred1 = self.model.predict(x_test_1)
        y_pred2 = self.model.predict(x_test_2)

        distance = None
        if distance_function == "euclidean":
            distance = np.linalg.norm(y_pred1 - y_pred2)
        else:
            raise NotImplementedError("Only `euclidean` distance function implemented at the moment.")

        return distance
