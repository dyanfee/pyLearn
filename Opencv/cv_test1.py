import cv2 as cv


img = cv.imread(".\\timg.jpg")
cv.namedWindow("Image")
cv.imshow("Image", img)
cv.waitKey(0)

cv.destroyAllWindows()
