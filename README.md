# Face Recognition using OpenCV - Python

This project aims to perform facial recognition using OpenCV and the Local Binary Patterns Histograms (LBPH) algorithm. 
The process involves three main steps:

## Step 1: Create a Dataset of Faces using Webcam
In this step, the dataset of faces is created using the webcam. Each person is assigned a unique ID (integer) to identify them in the dataset.

**Code:** [`dataset_creation.py`](dataset_creation.py)

## Step 2: Train the Recognizer using the Data Collected
The data collected in the previous step is used to train the facial recognition algorithm. The recognizer is trained on the dataset, and the trained data is stored in YML file format.

**Code:** [`training_dataset.py`](training_dataset.py)

## Step 3: Recognize Faces with the Trained Data
In the final step, the trained data from the YML file is imported, and the faces in the input images are recognized using the recognizer. The unique IDs are then associated with the names of the recognized individuals.

**Code:** [`face_recog.py`](face_recog.py)

## Requirements
- Python 3.x
- OpenCV library

## Usage
1. Run `dataset_creation.py` to create a dataset of faces using your webcam.
2. Run `training_dataset.py` to train the facial recognition algorithm with the collected data.
3. Run `face_recog.py` to recognize faces using the trained data.

## Contributions
Contributions and feedback are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
Feel free to use and modify this project for your facial recognition needs. Happy coding! 😄👍
