# Bitwise operation


import cv2 as cv
import numpy as np

img1 = cv.imread("Opencv/openImg.png")
img2 = cv.imread("Opencv/pause.png")


rows ,cols, channels = img2.shape
roi = img1[0:rows,0:cols]
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret,mask = cv.threshold(img2gray,175,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
img1_bg = cv.bitwise_and(roi,roi,mask = mask)
img2_fg = cv.bitwise_and (img2,img2,mask = mask_inv)
dst = cv.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv.imshow('Image',img1)
cv.waitKey(0)
cv.destroyAllWindows()