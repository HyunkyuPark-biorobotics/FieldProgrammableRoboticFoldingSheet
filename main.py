import os
import argparse
import numpy as np
from tensorflow.python.keras import optimizers

from tensorflow.python.keras.callbacks import EarlyStopping

from network import RNI_Network
from utils import load_dataset, save_history

os.environ["CUDA_VISIBLE_DEVICES"]="2"

if __name__ == '__main__':
	parser = argparse.ArgumentParser("Progammable Actuation RNI")

	parser.add_argument('--name', type=str, default='RNI_main_neutral_batch_256_lr_0.0001_NOISE_0.003', help='experiment name')
	parser.add_argument('--epochs', type=int, default=20000, help='epochs')
	parser.add_argument('--batch_size', type=int, default=256, help='batch size')
	parser.add_argument('--learning_rate', type=float, default=0.0001, help='Adam learning rate')
	parser.add_argument('--noise_level', type=float, default=0.003, help='noise level')
	args = parser.parse_args()

	# Load dataset
	path = "./dataset/dataset.mat"
	Input_set, Output_set = load_dataset(path, transpose=False)  # (num_samples, input_size)

	data_size = np.shape(Input_set)

	train_ratio = 0.85

	split_idx = int(data_size[0]*train_ratio)
	x_train = Input_set[:split_idx, :]
	x_valid = Input_set[split_idx:, :]

	y_train = Output_set[:split_idx, :]
	y_valid = Output_set[split_idx:, :]
	input_size = data_size[1]

	trn_mean = np.mean(x_train, 0)
	trn_std = np.std(x_train, 0)

	x_train = (x_train - trn_mean)/trn_std
	x_valid = (x_valid - trn_mean)/trn_std

	del Input_set, Output_set

	# Train network
	model = RNI_Network(input_size, 308, noise_level=args.noise_level/trn_std)
	optimizer = optimizers.Adam(lr=args.learning_rate, beta_1=0.9, beta_2=0.999)
	model.compile(loss='mse', optimizer=optimizer, metrics=['mse'])

	early_stopping = EarlyStopping(patience=100, restore_best_weights=True)
	hist = model.fit(x_train, y_train, epochs=args.epochs,verbose=2, batch_size=args.batch_size,
				  validation_data=(x_valid, y_valid), callbacks=[early_stopping])

	# Save network and results
	path = os.path.join("checkpoints", args.name)
	if not os.path.exists(path):
		os.mkdir(path)

	model.save(os.path.join(path,"model.h5"))
	save_history(os.path.join(path, "val_loss.txt"), hist.history["val_loss"])
	np.savetxt(os.path.join(path, "trn_mean.csv"), trn_mean, delimiter=",")
	np.savetxt(os.path.join(path, "trn_std.csv"), trn_std, delimiter=",")

#if __name__ == '__main__':
	#main()
