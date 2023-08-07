import os
from typing import Callable

import tensorflow as tf
from tensorflow.keras import metrics
from tensorflow.keras import Model

from useckit.paradigms.distance_learning.prediction_models.contrastive_loss.contrastive_model_description import \
    tower_mlp as tower_definition
from useckit.paradigms.distance_learning.prediction_models.offline_triplet_loss.triplet_distance_layer import \
    TrippleTowerDistanceLayer


class TrippleTowerModel(Model):
    """The Siamese Network model with a custom training and testing loops.

    Computes the triplet loss using the three embeddings produced by the
    Siamese Network.

    The triplet loss is defined as:
       L(A, P, N) = max(‖f(A) - f(P)‖² - ‖f(A) - f(N)‖² + margin, 0)
    """

    def __init__(self, tower_input_shape=None,
                 tower_model_description: Callable = tower_definition,
                 output_dir=None,
                 margin=0.5):
        super().__init__()
        self.tower_model_description = tower_model_description
        self.output_dir = output_dir

        if tower_input_shape is None:
            raise ValueError("Parameter `tower_input_shape` must be provided.")

        self.input_layer = tf.keras.layers.Input(tower_input_shape)

        self.tower_1 = self.tower_model_description(self.input_layer)  # anchor
        self.tower_2 = self.tower_model_description(self.input_layer)  # positive
        self.tower_3 = self.tower_model_description(self.input_layer)  # negative

        self.merge = TrippleTowerDistanceLayer()

        model_checkpoint = tf.keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(self.output_dir, 'best_model.hdf5'),
            monitor='loss',
            save_best_only=True,
            save_weights_only=True)
        self.callbacks = [model_checkpoint]

        self.compile(optimizer=tf.keras.optimizers.Adam(0.0001))

        self.margin = margin
        self.loss_tracker = metrics.Mean(name="loss")

    def call(self, inputs):
        x1 = self.tower_1(inputs[0])
        x2 = self.tower_2(inputs[1])
        x3 = self.tower_3(inputs[2])
        return self.merge(x1, x2, x3)

    def train_step(self, data):
        # GradientTape is a context manager that records every operation that
        # you do inside. We are using it here to compute the loss so we can get
        # the gradients and apply them using the optimizer specified in
        # `compile()`.
        with tf.GradientTape() as tape:
            loss = self._compute_loss(data)

        # Storing the gradients of the loss function with respect to the
        # weights/parameters.
        gradients = tape.gradient(loss, self.trainable_weights)

        # Applying the gradients on the model using the specified optimizer
        self.optimizer.apply_gradients(
            zip(gradients, self.trainable_weights)
        )

        # Let's update and return the training loss metric.
        self.loss_tracker.update_state(loss)
        return {"loss": self.loss_tracker.result()}

    def test_step(self, data):
        loss = self._compute_loss(data)

        # Let's update and return the loss metric.
        self.loss_tracker.update_state(loss)
        return {"loss": self.loss_tracker.result()}

    def _compute_loss(self, data):
        # The output of the network is a tuple containing the distances
        # between the anchor and the positive example, and the anchor and
        # the negative example.
        ap_distance, an_distance = self(data[0])

        # Computing the Triplet Loss by subtracting both distances and
        # making sure we don't get a negative value.
        loss = ap_distance - an_distance
        loss = tf.maximum(loss + self.margin, 0.0)
        return loss

    @property
    def metrics(self):
        # We need to list our metrics here so the `reset_states()` can be
        # called automatically.
        return [self.loss_tracker]
