#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np

'''
cv2.getTrackbarPos() 函数的一个参数是滑动条的名字，第二个参数
是滑动条被放置窗口的名字，第三个参数是滑动条的默认位置。第四个参数是
滑动条的最大值，第五个函数是回调函数，每次滑动条的滑动都会调用回调函
数。回调函数通常都会含有一个默认参数，就是滑动条的位置。
'''


def nothing(x):
    pass


img = np.zeros((300, 600, 3), np.uint8)
cv.namedWindow("Image")
# 创建滑动条
cv.createTrackbar('R', 'Image', 0, 255, nothing)
cv.createTrackbar('G', 'Image', 0, 255, nothing)
cv.createTrackbar('B', 'Image', 0, 255, nothing)
# 创建滑动条开关
switch = '0:OFF\n1:ON\n'
cv.createTrackbar(switch, 'Image', 0, 1, nothing)

while 1:
    cv.imshow('Image', img)
    k = cv.waitKey(1)
    if k == 27:
        break
    #     获取滑动条数据
    r = cv.getTrackbarPos('R', 'Image')
    g = cv.getTrackbarPos('G', 'Image')
    b = cv.getTrackbarPos('B', 'Image')
    s = cv.getTrackbarPos(switch, 'Image')

    if s == 0:
        img[:] = 0
    else: # 改变图片颜色
        img[:] = [b, g, r]
cv.destroyAllWindows()
