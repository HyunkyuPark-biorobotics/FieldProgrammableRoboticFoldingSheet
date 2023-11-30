import h5py
import numpy as np


def load_dataset(path, transpose=False):
    with h5py.File(path, "r") as h5py.Dataset:
        dataset_input = np.array(h5py.Dataset["/dataset/Input"])
        dataset_output = np.array(h5py.Dataset["/dataset/Output"])

        if transpose:
            dataset_input = np.transpose(dataset_input)
            dataset_output = np.transpose(dataset_output)

    return dataset_input, dataset_output


def save_history(path, history):
    np.savetxt(path, history, delimiter=",")
