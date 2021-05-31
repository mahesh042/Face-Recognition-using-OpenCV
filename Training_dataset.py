import cv2 as cv
import os
import numpy as np
from PIL import Image

recognizer = cv.face.LBPHFaceRecognizer_create()
detector = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
path = 'dataSet'


def getImageId(path):
    imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Id = []
    for img in imagepaths:
        face = Image.open(img).convert('L')
        facenp = np.array(face, 'uint8')
        imgId = int(os.path.split(img)[-1].split('.')[1])
        faces.append(facenp)
        Id.append(imgId)
        cv.imshow('training', facenp)
        cv.waitKey(1)
    return faces, np.array(Id)


faces, Id = getImageId(path)
recognizer.train(faces, Id)
recognizer.save('recognizer/trainingData.yml')
print('--------DATA TRAINED TO YML---------')
cv.destroyAllWindows()
