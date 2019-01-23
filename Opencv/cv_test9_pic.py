#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
# img = cv.imread("Pillow\\test.jpg")
img = cv.imread("Opencv/openImg.jpg")
# print(img)

# 获取行列处的 B G R 值 grey返回灰度值
px = img[100, 100]
# 单独获取RGB值
blue = img[100, 100, 0]
green = img[100, 100, 1]
red = img[100, 100, 2]
print(px)
print(blue, green, red)
# 修改某个行列处的值
img[100, 100] = [255, 255, 255]
px = img[100, 100]
print(px)

# 用numpy 修改计算矩阵 item：获取位置处的通道值
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

# 获取图像属性  shape:返回图像的行，列，通道
print(img.shape)
# img.size 返回图像的像素数目
print(img.size)
# img.dtype 返回图像的数据类型
print(img.dtype)

# 图像ROI
# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball

# 拆分通道 合并图像通道
# b, g, r = cv.split(img)
# 合并
# img = cv.merge([b,g,r])
# 或者 拆分通道
# b = [:,:,0]

# 红色通道值都设置为0
# img[:,:, 2] = 0

"""
# 描边 cv.copyMakeBorder()
src：源
top, bottom, left, right ：对应边像素数
borderType:
cv2.BORDER_CONSTANT  添加有颜色的常数值边界，还需要下一个参数（value）
cv2.BORDER_REFLECT  边界元素的镜像
cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT  跟上面一样，但稍作改动。例如: gfedcb|abcdefgh|gfedcba
cv2.BORDER_REPLICATE   重复最后一个元素
cv2.BORDER_WRAP   cdefgh|abcdefgh|abcdefg
"""
BLUE = [255, 0, 0]

img2 = cv.imread("Opencv/pause.png")

replicate = cv.copyMakeBorder(img2, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img2, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img2, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img2, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(
    img2, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img2, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WARP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title("CONSTANT")
plt.show()

# cv.imshow("Image", img2)

# cv.waitKey(0)

# cv.destroyAllWindows()
