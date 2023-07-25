# Face Recognition using OpenCV - Python
This project aims to perform facial recognition using OpenCV and the Local Binary Patterns Histograms (LBPH) algorithm. The process involves three main steps:

### Step 1: Create a Dataset of Faces using Webcam
In this step, the dataset of faces is created using the webcam. Each person is assigned a unique ID (integer) to identify them in the dataset.

Code: dataset_creation.py

### Step 2: Train the Recognizer using the Data Collected
The data collected in the previous step is used to train the facial recognition algorithm. The recognizer is trained on the dataset, and the trained data is stored in YML file format.

Code: Training_dataset.py

### Step 3: Recognize Faces with the Trained Data
In the final step, the trained data from the YML file is imported, and the faces in the input images are recognized using the recognizer. The unique IDs are then associated with the names of the recognized individuals.

Code: face_recog.py

Feel free to use and modify this project for your facial recognition needs. Happy coding! 😄👍


