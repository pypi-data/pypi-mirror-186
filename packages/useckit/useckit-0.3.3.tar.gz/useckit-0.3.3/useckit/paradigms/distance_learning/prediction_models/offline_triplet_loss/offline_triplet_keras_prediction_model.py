import os
import time
from typing import Callable, Tuple

import numpy as np
import tensorflow.keras as keras
from tensorflow.keras import metrics

from useckit.paradigms.distance_learning.prediction_models.distance_prediction_model_base import DistanceBasePredictionModel
from useckit.paradigms.distance_learning.prediction_models.contrastive_loss.contrastive_model_description import tower_mlp
from useckit.paradigms.distance_learning.prediction_models.offline_triplet_loss.triple_tower_model import TrippleTowerModel
from useckit.util.dataset import Dataset
from useckit.util.plotting import plot_history_df
from useckit.util.utils import triplet_make_pairs_random


class TripletKerasPredictionModel(DistanceBasePredictionModel):
    def __init__(self,
                 tower_model_description: Callable[[keras.layers.Input], keras.models.Model]
                 = tower_mlp,
                 merge_model_description: Callable[[keras.models.Model, keras.layers.Input,
                                                    keras.models.Model, keras.layers.Input,
                                                    keras.models.Model, keras.layers.Input],
                                                    keras.models.Model]
                 = None,
                 output_dir: str = "keras_pred_model_out",
                 verbose=False,
                 nb_epochs=10,
                 batch_size: Callable[[int], int] = 16,
                 pair_function: Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]] =
                 triplet_make_pairs_random):
        super().__init__(output_dir=output_dir, verbose=verbose)
        self.tower_model_description = tower_model_description
        self.merge_model_description = merge_model_description
        self.nb_epochs = 2000 if nb_epochs is None else nb_epochs
        assert isinstance(batch_size, Callable) or isinstance(batch_size, int)
        self.batch_size = batch_size
        self.callbacks = []
        self.model = None
        self.pair_function = pair_function
        self.loss_tracker = metrics.Mean(name="loss")

    def persist_model_trainables(self, path_like: str = 'saved_trainable_values', **kwargs):
        self.model.save_weights(os.path.join(self.output_dir, path_like))

    def restore_model_trainables(self,
                                 path_like: str,
                                 dataset: Dataset = None,
                                 pair_function: Callable[
                                     [np.ndarray, np.ndarray], Tuple[
                                         np.ndarray, np.ndarray]] = triplet_make_pairs_random,
                                 **kwargs):
        pairs_train, labels_train = pair_function(dataset.trainset_data, dataset.trainset_labels)

        x_train_1 = pairs_train[:, 0]
        input_shape = x_train_1.shape[1:]

        self.model = self.build_model(input_shape)
        self.model.load_weights(path_like)

    def build_model(self, input_shape, tower_model_description):
        return TrippleTowerModel(tower_input_shape=input_shape,
                                 tower_model_description=tower_model_description,
                                 output_dir=self.output_dir)

    def fit(self, dataset: Dataset):
        pairs_train, labels_train = self.pair_function(dataset.trainset_data, dataset.trainset_labels)

        # make validation pairs
        pairs_val, labels_val = self.pair_function(dataset.validationset_data, dataset.validationset_labels)

        input_shape_per_tower = tuple([] + [p for p in pairs_train.shape[2:]])
        input_shape_triple_tower_model = tuple([None] + [p for p in pairs_train.shape[1:]])

        y_train, y_val = labels_train, labels_val

        self.model = self.build_model(input_shape_per_tower, tower_model_description=self.tower_model_description)
        self.model.build(input_shape=input_shape_triple_tower_model)
        if self.verbose:
            print(self.model.summary())

        self.persist_model_trainables('model_init.hdf5')

        batch_size = self.batch_size

        start_time = time.time()
        hist = self.model.fit(x=pairs_train, y=y_train, batch_size=batch_size, epochs=self.nb_epochs,
                              verbose=self.verbose, validation_data=tuple([pairs_val, y_val]),
                              callbacks=self.model.callbacks)

        duration = time.time() - start_time
        plot_history_df(hist, self.output_dir)

        if self.verbose:
            print(f"Tripple tower distance learning model fitted in {round(duration, 2)} seconds!")

        self.persist_model_trainables('last_model.hdf5')
        # Not using restore here to not build a new model
        self.model.load_weights(os.path.join(self.output_dir, 'best_model.hdf5'))

        keras.backend.clear_session()

    def predict(self, x_test_1, x_test_2):
        y_pred = self.model.predict([x_test_1, x_test_2, x_test_2])
        ap_distance = y_pred[0]
        an_distance = y_pred[1]
        return np.maximum(ap_distance - an_distance, 0.0)
