import cv2 as cv
import numpy as np
# 读取图片
img = cv.imread("Pillow\\test.jpg")
# 设置为灰度图
# img = cv.cvtColor(img,   cv.COLOR_BGR2GRAY)
img = np.zeros(img.shape, np.uint8) # 创建图像
# img2 = img.copy() #复制图像
# img2[...] = 0 #转换为黑色图像
print(img)
cv.namedWindow("Image")
'''
cv.namedWindow("Image",x)
x = cv.WINDOW_AUTOSIZE #窗口自动大小 不可调整
x = cv.WINDOW_NORMAL #可调整窗口大小
'''
cv.imshow("Image", img)
cv.imwrite(".\\Opencv\\gray.jpg", img)  # 保存图片
cv.waitKey(0)  # 暂停按键等待

cv.destroyAllWindows()