# Field Programmable Robotic Folding Sheet


This repository contains code for the Resistive Network Imaiging (RNI) of feild-programmable Actuation RNI. 
## Overview

The code includes:

- `main.py`: Script to train the RNI model on a given dataset.
- `modules/RNI_Network.py`: Contains the implementation of the RNI neural network.
- `utils/utils.py`: Utility functions for loading datasets, saving history, etc.

## Requirements

- Python 3.x
- TensorFlow
- NumPy

## Usage

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/HyunkyuPark-biorobotics/Field_Programmable_Robotic_Folding_Sheet.git
    cd Field_Programmable_Robotic_Folding_Sheet
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Training

Run the training script with specified arguments:

```bash
python main.py --name <experiment_name> --epochs <num_epochs> --batch_size <batch_size> --learning_rate <learning_rate> --noise_level <noise_level>
```

Replace `<experiment_name>`, `<num_epochs>`, `<batch_size>`, `<learning_rate>`, `<noise_level>` with your desired values.

### Arguments

- `--name`: Experiment name for saving results.
- `--epochs`: Number of training epochs.
- `--batch_size`: Batch size for training.
- `--learning_rate`: Learning rate for the Adam optimizer.
- `--noise_level`: Level of input noise.

### Output
Following data is saved in the 'checkpoints' directory.
1) The trained model
2) validation loss history
3) mean /standard deviation of the training data normalization 

## Dataset

The dataset is synthesized by MATLAB, stored as '.mat' format.
Please download the file from the following link:


---

Remember to fill in placeholders such as `<experiment_name>`, `<num_epochs>`, and `<batch_size>` with appropriate values and to include any additional details or instructions specific to your project.
