from PIL import Image
from PIL import ImageFilter
im = Image.open("E:\VsCode\Python\Pillow\\test.jpg")
print(im.mode)
rgb2xyz = (0.412453, 0.357580, 0.180423, 0,
           0.212671, 0.715160, 0.072169, 0,
           0.019334, 0.119193, 0.950227, 0)
new_im = im.convert("L", rgb2xyz)
print(new_im.mode)
print(im.size)
new_im.save("test2.jpg")
# new_im.show()
bluF = im.filter(ImageFilter.BLUR)  # 均值滤波
conF = im.filter(ImageFilter.CONTOUR)  # 找轮廓
edgeF = im.filter(ImageFilter.FIND_EDGES)  # 边缘检测
im.show()
bluF.show()
conF.show()
edgeF.show()
