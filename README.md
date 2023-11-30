# Field-Programmable Robotic Folding Sheet


This repository contains code for Resistive Network Imaging (RNI) of field-Programmable Robotic Folding Sheet. 
![image](https://github.com/HyunkyuPark-biorobotics/FieldProgrammableRoboticFoldingSheet/assets/44401853/4a1e3789-8d24-47b2-bcc4-9362d35048c8)

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
    git clone https://github.com/HyunkyuPark-biorobotics/FieldProgrammableRoboticFoldingSheet.git
    cd FieldProgrammableRoboticFoldingSheet
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

https://drive.google.com/file/d/10gqsUo3axfFWQx3C_yWNRf0NdhoKSaQ6/view?usp=drive_link

---

Remember to fill in placeholders such as `<experiment_name>`, `<num_epochs>`, and `<batch_size>` with appropriate values and to include any additional details or instructions specific to your project.
