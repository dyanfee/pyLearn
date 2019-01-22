#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np
'''
 实现 点击绘制矩形 按下m绘制曲线(圆圈连接在一起)
'''
down = False
# 按下 m 绘制曲线 为True时绘制矩形
mode = False
ix, iy = -1, -1
# 回调函数
def draw_circle(event,x,y,flags,param):
    global  ix,iy,down,mode
    # 按下左键 回到起始坐标
    if event == cv.EVENT_LBUTTONDOWN:
        down = True
        ix,iy = x,y
    #     按下左键并移动 绘制图形
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        if down == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(255,255,255),-1)
            else:
                # 绘制圆圈
                cv.circle(img,(x,y),3,(0,255,255),-1,cv.LINE_AA)
                # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
                # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                # cv2.circle(img,(x,y),r,(0,0,255),-1)
        elif event == cv.EVENT_LBUTTONUP:
            down = False
img  = np.zeros((600,800,3),np.uint8)
cv.namedWindow("Image")
cv.setMouseCallback("Image",draw_circle)
while 1:
    cv.imshow("Image",img)
    k = cv.waitKey(1)
    if k == ord("m"):
        mode = not mode
    elif k == 27:
        break

