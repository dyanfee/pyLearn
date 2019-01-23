import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
'''
• In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is
more preferable. MJPG results in high size video. X264 gives
very small size video)
• In Windows: DIVX (More to be tested and added)
• In OSX : (I don’t have access to OSX. Can some one fill this?)
'''
out = cv.VideoWriter(".\\output.avi", fourcc, 20, 0, (640, 480))
# TODO:test
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # frame = cv.flip(frame,0) #翻转视频
        out.write(frame)
        cv.imshow("frame", frame)
        if cv.waitKey(1) == ord("q") or cv.waitKey(1) == "37":
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
