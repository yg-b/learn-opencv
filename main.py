import cv2 as cv
import sys

img = cv.imread("image/8326cffc1e178a82b901304d9955648da9773812429d.jpg")
if img is None:
    sys.exit("无法读取图像")
cv.imshow("show window",img)
k = cv.waitKey(0)
if k == ord ("s"):
    cv.imwrite("image/test.jpg",img)
