import cv2 as cv
import os


def capture(name, source=cv.CAP_DSHOW):
    root = os.path.join('..', 'resources')

    video = cv.VideoCapture(source)
    mode = True
    sent = 'Activated'
    success = False
    if source == cv.CAP_DSHOW:
        mode = False
        sent = 'Press enter to start capturing '
    i = 0
    while(1):
        _, frame = video.read()
        frame = cv.flip(frame, 1)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
        if k == 13:
            sent = 'Activated'
            mode = True

        if mode:
            cv.imwrite(os.path.join(root, name, str(i)+'.jpg'), frame)
            i += 1
        if i == 1000:
            success = True
            break
        frame = cv.resize(frame, (480, 640))
        cv.putText(frame, sent, (0, 470), cv.FONT_HERSHEY_COMPLEX_SMALL,
                   1, (0, 0, 255), 2, cv.LINE_8)
        cv.imshow('Capture', frame)

    cv.destroyAllWindows()
    video.release()
    return success
