import cv2 as cv

faceCascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt2.xml")
video_capture = cv.VideoCapture(0)

Id = 0
num = 0

while True:
    try:
        Id = int(input("Enter Id number for your face: "))
        print("------------Preparing DataSet for id number :", Id)
        break
    except ValueError:
        print("------------Please input integer only-------------")
        continue

while True:
    ret, frame = video_capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                         flags=cv.CASCADE_SCALE_IMAGE)
    for (x, y, width, height) in faces:
        num = num + 1
        cv.imwrite('dataSet/user.' + str(Id) + '.' + str(num) + '.jpg', gray[y:y + height, x:x + width])
        cv.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        cv.waitKey(100)
    cv.imshow('Video', frame)
    cv.waitKey(20)
    if num > 50:
        break

print('---------DATASET CREATED-----------')
video_capture.release()
cv.destroyAllWindows()
