import cv2
import numpy as np
cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key ==27:
        break