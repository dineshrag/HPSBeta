import cv2
import numpy as np
def nothing(x):
    pass
while True:
    frame = cv2.imread('C://Users//raghu//Desktop//PythonWorkspace//ImageClassification_DL//Data//frame0.jpg')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_b = np.array([0, 0, 237])
    u_b = np.array([195, 26, 255])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key ==27:
        break
