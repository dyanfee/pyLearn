import cv2 as cv
import numpy as np

# cv.warpAffine() 2*3 变换矩阵
# cv.warpPerspective()  3*3 变换矩阵

# cv.resize() 改变尺寸
# 缩放插值方法 cv.INTER_AREA cv.INTER_CUBIC cv.INTER_LINEAR

img = cv.imread("Opencv/girl.png")
res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)


height, width = img.shape[:2]  # 截取数组前两位 shape(height,width,通道)
print(img.shape)
print(height, width)
res = cv.resize(img, (2*width, 2*height), interpolation=cv.INTER_CUBIC)

while 1:
    cv.imshow("res", res)
    cv.imshow("img", img)
    if cv.waitKey(1) == 27:
        break
cv.destroyAllWindows()
