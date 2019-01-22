#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np
'''
    画一条简单线段
'''

img = np.zeros((512,512,3),np.uint8)
'''
img:绘制的图像
opt1:起点
opt2:终点
color:绘制的颜色
thickness:线条的粗细
linetype:线条的类型 cv2.LINE_AA 抗锯齿
'''
# 画线
cv.line(img,(0,0),(511,511),(255,255,255),5)
# 画矩形 opt1 左上顶点 opt2 右下顶点
cv.rectangle(img,(300,0),(400,200),(0,0,255),3)
# 画圆 center:圆心 radius:半径
cv.circle(img,(300,400),70,(0,128,0),-1,cv.LINE_AA)
# 画椭圆 圆心 长短轴 旋转角度 起始角度 终止角度 颜色
cv.ellipse(img,(120,400),(100,50),0,0,360,255,-1,cv.LINE_AA)
# 画多边形 [[10,5],[20,30],[70,20],[50,10]]
pts = np.array([[10,5],[200,300],[270,400],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
# 这里 reshape 的第一个参数为 -1, 表明这一维的长度是根据后面的维度的计算出来的。
cv.polylines(img,pts,True,(255,22,255),10)
# 绘制文字
font  = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"OpenCV",(10,300),font,4,(255,255,0),2,cv.LINE_AA)


cv.imshow("line",img)
cv.waitKey(0)

cv.destroyAllWindows()