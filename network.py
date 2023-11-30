from tensorflow.keras.layers import (
    Activation,
    BatchNormalization,
    Dense,
    GaussianNoise,
    Input,
)
from tensorflow.keras.models import Model


class RNINetwork(Model):
    def __init__(self, input_size, output_size, noise_level=0):
        super().__init__()
        self.gaussian_noise = GaussianNoise(noise_level, input_shape=(input_size,))
        self.dense1 = Dense(output_size)
        self.batch_norm1 = BatchNormalization()
        self.activation1 = Activation("relu")

        self.dense2 = Dense(output_size)
        self.batch_norm2 = BatchNormalization()
        self.activation2 = Activation("relu")

        self.dense3 = Dense(output_size)

    def call(self, inputs, training=False):
        x = self.gaussian_noise(inputs)

        x = self.dense1(x)
        x = self.batch_norm1(x, training=training)
        x = self.activation1(x)

        x = self.dense2(x)
        x = self.batch_norm2(x, training=training)
        x = self.activation2(x)

        return self.dense3(x)
