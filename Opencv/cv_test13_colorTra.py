import cv2 as cv
import numpy as np

# cv2.cvtColor(input_image ，flag)
# img = cv.imread("Opencv/girl.png")

# img2 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# H（色彩/色度）的取值范围是 [0，179]
# S（饱和度）的取值范围 [0，255]
# V（亮度）的取值范围 [0，255]
# img1 = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# flags = [i for i in dir(cv) if 'COLOR_' in i ]
# print(flags)

cap = cv.VideoCapture(0)

# 查找颜色HSV值
green = np.uint8([[[0, 0, 255]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)


# 跟踪红色物体
while 1:
    # 获取每一帧
    ret, frame = cap.read()
    # 每一帧画面转HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 设定跟踪颜色的值
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([60, 255, 255])

    # 阈值 建模   ---------------
    mask = cv.inRange(hsv, lower_red, upper_red)

    # 对原图像和掩模进行位运算 -------------
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5)
    if k == 27:
        break

cv.destroyAllWindows()
