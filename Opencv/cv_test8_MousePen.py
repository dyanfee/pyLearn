#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np


event = [i for i in dir(cv) if 'EVENT' in i]
print(event)
'''
['EVENT_FLAG_ALTKEY',
'EVENT_FLAG_CTRLKEY',
'EVENT_FLAG_LBUTTON',
'EVENT_FLAG_MBUTTON', 
'EVENT_FLAG_RBUTTON', 
'EVENT_FLAG_SHIFTKEY', 
'EVENT_LBUTTONDBLCLK',
'EVENT_LBUTTONDOWN', 
'EVENT_LBUTTONUP', 
'EVENT_MBUTTONDBLCLK',
'EVENT_MBUTTONDOWN', 
'EVENT_MBUTTONUP', 
'EVENT_MOUSEHWHEEL', 
'EVENT_MOUSEMOVE', 
'EVENT_MOUSEWHEEL',
'EVENT_RBUTTONDBLCLK',
'EVENT_RBUTTONDOWN',
'EVENT_RBUTTONUP']
'''
# 点击位置绘制圆圈
def draw_circle(event,x,y,flags,param):
    # print("enter!!")
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,255,255),-1,cv.LINE_AA)
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow("image")
cv.setMouseCallback("image",draw_circle)

while 1:
    cv.imshow("image",img)
    if cv.waitKey(20) == 27:
        break
cv.destroyAllWindows()
