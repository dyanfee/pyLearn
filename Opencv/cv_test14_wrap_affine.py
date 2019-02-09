import cv2 as cv
import numpy as np

# cv.warpAffine() 平移

img = cv.imread("Opencv/girl.png")
# matrix 矩阵
H = np.float32([[1, 0, 100], [0, 1, 50]])
rows, cols = img.shape[:2]
res = cv.warpAffine(img, H, (rows, cols))

cv.imshow("Image", img)
cv.imshow("res", res)

cv.waitKey(0)
cv.destroyAllWindows()
