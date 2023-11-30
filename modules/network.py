from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import GaussianNoise
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import BatchNormalization
from tensorflow.python.keras.layers import Activation

def RNI_Network(input_size, output_size, noise_level=0):
	model = Sequential()

	model.add(GaussianNoise(noise_level, input_shape=(input_size,)))

	model.add(Dense(output_size))
	model.add(BatchNormalization())
	model.add(Activation('relu'))

	model.add(Dense(output_size))
	model.add(BatchNormalization())
	model.add(Activation('relu'))

	#model.add(Dense(output_size))
	#model.add(BatchNormalization())
	#model.add(Activation('relu'))


	model.add(Dense(output_size))

	return model

