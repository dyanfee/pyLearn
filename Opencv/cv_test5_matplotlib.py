from matplotlib import pyplot as plt
import cv2 as cv


img = cv.imread("Opencv\\saveTest.png")  # Opencv 颜色模式为BGR  matplotlib 颜色模式为RGB
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([]), plt.yticks([])  # 隐藏标尺
plt.show()

'''
1、RGB和BGR（opencv默认的彩色图像的颜色空间是BGR）颜色空间的转换
cv.COLOR_BGR2RGB cv.COLOR_RGB2BGR cv.COLOR_RGBA2BGRA cv.COLOR_BGRA2RGBA

2、向RGB和BGR图像中增添alpha通道
cv.COLOR_RGB2RGBA cv.COLOR_BGR2BGRA

3、从RGB和BGR图像中去除alpha通道
cv.COLOR_RGBA2RGB cv.COLOR_BGRA2BGR

4、从RBG和BGR颜色空间转换到灰度空间
cv.COLOR_RGB2GRAY cv.COLOR_BGR2GRAY
cv.COLOR_RGBA2GRAY cv.COLOR_BGRA2GRAY

5、从灰度空间转换到RGB和BGR颜色空间
cv.COLOR_GRAY2RGB
cv.COLOR_GRAY2BGR

cv.COLOR_GRAY2RGBA
cv.COLOR_GRAY2BGRA

6、RGB和BGR颜色空间与BGR565颜色空间之间的转换
cv.COLOR_RGB2BGR565
cv.COLOR_BGR2BGR565
cv.COLOR_BGR5652RGB
cv.COLOR_BGR5652BGR
cv.COLOR_RGBA2BGR565
cv.COLOR_BGRA2BGR565
cv.COLOR_BGR5652RGBA
cv.COLOR_BGR5652BGRA

7、灰度空间域BGR565之间的转换
cv.COLOR_GRAY2BGR555
cv.COLOR_BGR5552GRAY

8、RGB和BGR颜色空间与CIE XYZ之间的转换
cv.COLOR_RGB2XYZ
cv.COLOR_BGR2XYZ
cv.COLOR_XYZ2RGB
cv.COLOR_XYZ2BGR

9、RGB和BGR颜色空间与uma色度（YCrCb空间）之间的转换
cv.COLOR_RGB2YCrCb
cv.COLOR_BGR2YCrCb
cv.COLOR_YCrCb2RGB
cv.COLOR_YCrCb2BGR

10、RGB和BGR颜色空间与HSV颜色空间之间的相互转换
cv.COLOR_RGB2HSV
cv.COLOR_BGR2HSV
cv.COLOR_HSV2RGB
cv.COLOR_HSV2BGR

11、RGB和BGR颜色空间与HLS颜色空间之间的相互转换
cv.COLOR_RGB2HLS
cv.COLOR_BGR2HLS
cv.COLOR_HLS2RGB
cv.COLOR_HLS2BGR

12、RGB和BGR颜色空间与CIE Lab颜色空间之间的相互转换
cv.COLOR_RGB2Lab
cv.COLOR_BGR2Lab
cv.COLOR_Lab2RGB
cv.COLOR_Lab2BGR

13、RGB和BGR颜色空间与CIE Luv颜色空间之间的相互转换
cv.COLOR_RGB2Luv
cv.COLOR_BGR2Luv
cv.COLOR_Luv2RGB
cv.COLOR_Luv2BGR

14、Bayer格式（raw data）向RGB或BGR颜色空间的转换
cv.COLOR_BayerBG2RGB
cv.COLOR_BayerGB2RGB
cv.COLOR_BayerRG2RGB
cv.COLOR_BayerGR2RGB
cv.COLOR_BayerBG2BGR
cv.COLOR_BayerGB2BGR
cv.COLOR_BayerRG2BGR
cv.COLOR_BayerGR2BGR

'''
