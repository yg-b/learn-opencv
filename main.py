import numpy as np
import cv2 as cv

draw = False
ix,iy= -1,-1
lock = True
r,g,b,size = 0,0,0,1

def get_cz(val):
    global r,g,b,size
    r = cv.getTrackbarPos('R','color and size')
    g = cv.getTrackbarPos('G','color and size')
    b = cv.getTrackbarPos('B','color and size')
    size = cv.getTrackbarPos('Size','color and size')
    color_size_img[:] = [b,g,r]

def color_size():
    global switch
    cv.createTrackbar('R','color and size',0,255,get_cz)
    cv.createTrackbar('G','color and size',0,255,get_cz)
    cv.createTrackbar('B','color and size',0,255,get_cz)
    cv.createTrackbar('Size','color and size',1,6,get_cz)

def draw_line(event,x,y,flags,param):
    global draw,ix,iy,lock

    if event == cv.EVENT_LBUTTONDOWN:
        draw = True
        ix = x
        iy = y
    
    elif event == cv.EVENT_MOUSEMOVE:
        if draw == True:
            img_temp = img.copy()
            lock = False
            cv.line(img_temp,(ix,iy),(x,y),(b,g,r),size)
            cv.imshow('image',img_temp)

    elif event == cv.EVENT_LBUTTONUP:
        draw = False
        cv.line(img,(ix,iy),(x,y),(b,g,r),size)

img = np.zeros((512,512,3), np.uint8)
color_size_img = np.zeros((200,200,3), np.uint8)
cv.namedWindow('image')
cv.namedWindow('color and size')
color_size()
cv.setMouseCallback('image',draw_line)

while(1):
    if lock == True:
        cv.imshow('image',img)
    cv.imshow('color and size',color_size_img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()