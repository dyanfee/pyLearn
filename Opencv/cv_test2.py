import cv2 as cv
# 读取图片
img = cv.imread("Pillow\\test.jpg")
# 设置为灰度图
img = cv.cvtColor(img,   cv.COLOR_BGR2GRAY)
cv.namedWindow("Image")
cv.imshow("Image", img)
cv.imwrite(".\\Opencv\\gray.jpg", img)  # 保存图片
cv.waitKey(0)  # 暂停按键等待
