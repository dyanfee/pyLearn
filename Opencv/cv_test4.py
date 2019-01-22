import cv2 as cv

img = cv.imread("Pillow\\test.jpg")
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27: # ESC
    cv.destroyAllWindows()
elif k == ord("s"): # s
    cv.imwrite("Opencv\\saveTest.png",img) #保存
    cv.destroyAllWindows()