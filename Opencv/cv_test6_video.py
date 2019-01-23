import cv2 as cv
a = 0
cap = cv.VideoCapture(0)
while(True):
    ret, frame = cap.read()  # 读取每一帧数据

    # cap.isOpened() #摄像头是否成功初始化
    # cap.open() #初始化摄像头
    # cap.get(propId) #获得视频的一些参数信息 propId：0-18 的整数 每一个数代表视频的一个属性
    # ret = cap.set(3, 320)
    # ret = cap.set(4, 240) 来把宽和高改成 320X240。 更多参数如下
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', frame)
    a += 1
    name = "Opencv\\cvideo"+str(a)+".jpg"
    cv.imwrite(name, frame)
    if cv.waitKey(1) == ord("q"):
        break

# release
cap.release()
cv.destroyAllWindows()


'''
• CV_CAP_PROP_POS_MSEC Current position of the video file
in milliseconds.
• CV_CAP_PROP_POS_FRAMES 0-based index of the frame to
be decoded/captured next.
• CV_CAP_PROP_POS_AVI_RATIO Relative position of the
video file: 0 - start of the film, 1 - end of the film.
• CV_CAP_PROP_FRAME_WIDTH Width of the frames in the
video stream.
• CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the
video stream.
• CV_CAP_PROP_FPS Frame rate.
• CV_CAP_PROP_FOURCC 4-character code of codec.
• CV_CAP_PROP_FRAME_COUNT Number of frames in the
video file.
• CV_CAP_PROP_FORMAT Format of the Mat objects returned
by retrieve() .
• CV_CAP_PROP_MODE Backend-specific value indicating the
current capture mode.
• CV_CAP_PROP_BRIGHTNESS Brightness of the image (only
for cameras).
• CV_CAP_PROP_CONTRAST Contrast of the image (only for
cameras).
• CV_CAP_PROP_SATURATION Saturation of the image (only
for cameras).
• CV_CAP_PROP_HUE Hue of the image (only for cameras).
• CV_CAP_PROP_GAIN Gain of the image (only for cameras).
• CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
• CV_CAP_PROP_CONVERT_RGB Boolean flags indicating
whether images should be converted to RGB.
• CV_CAP_PROP_WHITE_BALANCE Currently unsupported
• CV_CAP_PROP_RECTIFICATION Rectification flag for stereo
cameras (note: only supported by DC1394 v 2.x backend cur-
rently)
'''