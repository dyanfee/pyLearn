from MyQR import myqr
# myqr.run(" i hate you ")
''' 彩色底色二维码 '''
# myqr.run(words='https://www.baidu.com',
#          picture='MyQR/wm.jpg',
#          colorized=True, #是否彩色显示
#          save_name='MyQR/test3.png')
''' gif 二维码 '''
myqr.run(words='http://www.mmjpg.com/hot/',
         picture='MyQR/wm.gif',
         colorized=True, #是否彩色显示
         save_name='MyQR/test5.gif')