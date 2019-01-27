import cv2 as cv
import numpy as np

# cv.warpAffine() 平移

img = cv.imread("Opencv/girl.png")
# matrix 矩阵
res = cv.warpAffine(img,)