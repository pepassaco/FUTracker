# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
import numpy as np

cap = cv2.VideoCapture('1.mp4')


#fgbg2 = cv2.createBackgroundSubtractorMOG2()
fgbg3 = cv2.bgsegm.createBackgroundSubtractorCNT()

    


while(1):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=500)


    #fgmask2 = fgbg2.apply(frame)
    fgmask3 = fgbg3.apply(frame)
   
   
    #cv2.imshow('2',fgmask2)
    cv2.imshow('3',fgmask3)



    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()