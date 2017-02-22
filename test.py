#!/usr/bin/env python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#cv2.namedWindow("RGB")
cv2.namedWindow("RGB_Processed")
#cv2.namedWindow("HSV")

status, img = cap.read()
h, w = img.shape[:2]

avg = np.float32(img)
lowThresh = 100
highThresh = 250



# mouse event to get pixel values at clicked pixel
def getPixels(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        px = hsvImg[x,y]
        print(px)

# track movement
def trackMovement():
    img = cap.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRY)
    image1 = img
    difference = img
    while True:
        img = cap.read()
        img 

# while loop for showing live videos
while True:
    # images directly from webcam
    status, img = cap.read()
    # image converted to hsv
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 
    # blur
    processed = cv2.GaussianBlur(img,(11,11),0)

    # get background
    cv2.accumulateWeighted(img,avg,0.01)
    background = cv2.convertScaleAbs(avg)

    # subtract background
    processed = img - background
    processed = cv2.cvtColor(processed,cv2.COLOR_BGR2GRAY)
    retval, processed = cv2.threshold(processed, lowThresh, 255, cv2.THRESH_BINARY)
    processed = cv2.GaussianBlur(processed,(5,5),0)
    retval, processed = cv2.threshold(processed, highThresh, 255, cv2.THRESH_BINARY)
    im2, contours, hierarchy = cv2.findContours(processed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        for coo in c:
            minx = w
            maxx = 0
            miny = h
            maxy = 0        
            for co in coo:
#                print(co[0])
                if co[0] < minx:
                    minx = co[0]
                if co[0] > maxx:
                    maxx = co[0]
                if co[1] < miny:
                    miny = co[1]
                if co[1] > maxy:
                    maxy = co[1]
        print(minx,maxx,miny,maxy)




    # brighten
#    h, s, v = cv2.split(hsvImg)
#    v += 100
#    if v.any() > 255:
#        v = 255
#    endHSV = cv2.merge((h, s, v))
#    processed = cv2.cvtColor(endHSV, cv2.COLOR_HSV2BGR)
    
    # show both windows
#    cv2.imshow("RGB", img)
    cv2.imshow("RGB_Processed", im2)
#    cv2.imshow("HSV", hsvImg)
    k = cv2.waitKey(1)
    if k == 27:
        break
    # check for mouse event
    cv2.setMouseCallback("HSV", getPixels)

cv2.destroyAllWindows()

