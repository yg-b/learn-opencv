import numpy as np
import cv2 as cv
import sys

def draw_circle(event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img,(x,y),100,(255,0,0),-1)

img = cv.imread("image/test.jpg")
if img is None:
    sys.exit("can not do")
#events = [i for i in dir(cv) if 'EVENT' in i]
#print(events)
cv.namedWindow('image')
cv.setMouseCallback ( 'image' , draw_circle)
cv.line(img,(0,0),(511,511),(255,0,0),5)
while True:
    cv.imshow("image",img)
    k = cv.waitKey(1)
    if k == ord("q"):
         break
cv.destroyAllWindows()