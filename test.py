#!/usr/bin/env python3

import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("RGB")
cv2.namedWindow("HSV")
# get images
status, img = cap.read()
# get HSV image from inputted image
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def getPixels(event, x, y, flags, param):    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(hsvImg.getPixel(x, y))

while True:
        # show images
    cv2.imshow("RGB", img)
    cv2.imshow("HSV", hsvImg)
    # not sure what this does yet
    k = cv2.waitKey(1)
    if k == 27:
        break
    cv2.setMouseCallback("HSV", getPixels)

cv2.destroyAllWindows()

