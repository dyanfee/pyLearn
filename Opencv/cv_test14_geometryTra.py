import cv2 as cv
import numpy as np

# cv.warpAffine() 2*3 变换矩阵
# cv.warpPerspective()  3*3 变换矩阵

# cv.resize() 改变尺寸
# 缩放插值方法 cv.INTER_AREA cv.INTER_CUBIC cv.INTER_LINEAR

img =cv.imread("Opencv/girl.png")
res = cv.resize(img,fx=2,fy=2,interpolation)