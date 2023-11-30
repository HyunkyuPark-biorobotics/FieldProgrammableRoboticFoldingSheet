import numpy as np
import h5py

def load_dataset(path, transpose=False):
	Dataset = h5py.File(path)
	dataset = Dataset['dataset']
	dataset_input = dataset['/dataset/Input'].value
	dataset_output = dataset['/dataset/Output'].value
	if transpose:
		dataset_input = np.transpose(dataset_input)
		dataset_output = np.transpose(dataset_output)

	return dataset_input, dataset_output

def save_history(path, history):
	np.savetxt(path, history, delimiter=",")

