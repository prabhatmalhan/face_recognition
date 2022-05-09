from ast import Str
import cv2


def get_face(image: Str):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    img = cv2.imread(image)
    img = cv2.resize(img, (352, 640))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = cv2.resize(gray[y:y+h, x:x+w], (100, 100))
        # roi_color = cv2.resize(img[y:y+h, x:x+w], (100, 100))
    try:
        return (True,roi_gray)
    except:
        return (False,None)
