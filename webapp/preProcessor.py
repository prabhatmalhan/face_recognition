import cv2


def get_face(img):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_color = cv2.resize(img[y:y+h, x:x+w], (100, 100))
    shape = img.shape
    if shape[0] < shape[1]:
        img = cv2.resize(img, (320, 176))
    else:
        img = cv2.resize(img, (176, 320))
    try:
        return (True, img, roi_color)
    except:
        return (False, img, None)
