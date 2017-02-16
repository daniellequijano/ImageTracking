#!/usr/bin/env python3

import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("RGB")
cv2.namedWindow("HSV")

while True:

    status, img = cap.read()
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("RGB", img)
    cv2.imshow("HSV", hsvImg)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()

