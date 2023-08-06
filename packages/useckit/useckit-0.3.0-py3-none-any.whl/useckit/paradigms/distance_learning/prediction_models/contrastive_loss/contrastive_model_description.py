import tensorflow as tf
import tensorflow_addons as tfa
from tensorflow import keras
from tensorflow.keras import layers


def tower_mlp(input_layer: keras.layers.Input) -> keras.models.Model:
    x = tf.keras.layers.BatchNormalization()(input_layer)
    x = layers.Dense(200, activation="tanh")(x)
    x = layers.Dense(100, activation="tanh")(x)
    x = layers.Flatten()(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = layers.Dense(50, activation="relu")(x)
    return keras.Model(input_layer, x)

def tower_conv_2d(input_layer: keras.layers.Input) -> keras.models.Model:
    x = tf.keras.layers.BatchNormalization()(input_layer)
    x = layers.Conv2D(4, (5, 5), activation="tanh")(x)
    x = layers.AveragePooling2D(pool_size=(2, 2))(x)
    x = layers.Conv2D(16, (5, 5), activation="tanh")(x)
    x = layers.AveragePooling2D(pool_size=(2, 2))(x)
    x = layers.Flatten()(x)

    x = tf.keras.layers.BatchNormalization()(x)
    x = layers.Dense(10, activation="tanh")(x)
    return keras.Model(input_layer, x)


def merge_constractive(tower_1: keras.models.Model, input_1: keras.layers.Input,
                       tower_2: keras.models.Model, input_2: keras.layers.Input) -> keras.models.Model:
    merge_layer = tf.linalg.norm((tower_1(input_1) - tower_2(input_2)), axis=1, keepdims=True)
    normal_layer = tf.keras.layers.BatchNormalization()(merge_layer)
    output_layer = layers.Dense(1, activation="sigmoid")(normal_layer)
    result = keras.Model(inputs=[input_1, input_2], outputs=output_layer)

    result.compile(loss=tfa.losses.contrastive_loss, optimizer="RMSprop", metrics=["accuracy"])
    return result


