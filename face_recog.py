import cv2 as cv

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/trainingData.yml')
faceCascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt2.xml")
video_capture = cv.VideoCapture(0)
Id = 0

while True:
    ret, frame = video_capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                         flags=cv.CASCADE_SCALE_IMAGE)
    for (x, y, width, height) in faces:
        cv.rectangle(frame, (x, y), (x + width, y + height), (0, 225, 0), 2)
        Id, confidence = recognizer.predict(gray[y:y + height, x:x + width])
        if confidence < 50:
            if Id == 1:
                Id = 'Mahesh'

            elif Id == 2:
                Id = 'RAJU'
        else:
            Id = 'unknown'

        font = cv.FONT_HERSHEY_DUPLEX
        cv.putText(frame, str(Id), (x, y+height), font, 1.25, (0, 0, 225), 3)

    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

video_capture.release()
cv.destroyAllWindows()
