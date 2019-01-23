#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np

# cv.add()  res=img1+img

x = np.uint8([250])
y = np.uint8([10])
print(cv.add(x, y))  # 250+10 = 260 => 255
print(x + y)  # 250+10 = 260 % 256 = 4

# image mixing
# g (x) = (1 − α)f 0 (x) + αf 1 (x)
# test mixing

img1 = cv.imread("Opencv/play.png")
img2 = cv.imread("Opencv/pause.png")
# print(img1, img2)
# dst = α · img1 + β · img2 + γ
dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

cv.imshow("Image1", img1)
cv.imshow("Image", dst)
cv.waitKey(0)
cv.destroyAllWindows()
