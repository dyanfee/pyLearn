import cv2 as cv
import numpy as np


img1 = cv.imread("Opencv/girl.png")
# cv.getTickCount  获取时间 从参考点开始 time.time()
# cv.getTickFrequency 获取时钟频率 （帧率）

e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)  # 中值滤波
e2 = cv.getTickCount()
time = (e2 - e1) / cv.getTickFrequency()
print(time)

# 函数优化 返回是否开启优化
print(cv.useOptimized())

# cv.setUseOptimized() 开启优化
# cv2.countNonZero() 和 np.count_nonzero()
cv.imshow("Image", img1)
cv.waitKey(0)
cv.destroyAllWindows()
