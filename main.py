import numpy as np
import cv2 as cv

drawing = False
mode = True
ix,iy = -1,-1
lock = -1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,lock

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            lock = 0
            if mode == True:
                img_temp = img.copy()
                cv.rectangle(img_temp,(ix,iy),(x,y),(0,255,0),1)
                cv.imshow("image",img_temp)
            else:
                cv.circle(img_temp,(x,y),5,(0,0,255),1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        lock = -1
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

while(1):
    if lock == -1:
        cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv.destroyAllWindows()