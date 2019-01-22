from PIL import Image

url = input("输入图片地址：")
img = Image.open(url)
out = img.convert("L")
width, height = out.size
print("图片的宽高为：%d × %d" % (width, height))
rate = float(input("输入缩放比例："))
vscale = float(input("垂直比例系数："))
out = out.resize((int(width*rate), int(height*rate*vscale)))
width, height = out.size
print("图片的宽高为：%d × %d" % (width, height))
asciis = "@#%/*^+=-'. "
texts = ""
lens = len(asciis) - 1
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col, row))
        texts += asciis[int(gray/255 * lens)]
    texts += "\n"
with open("result.txt", "w") as f:
    f.write(texts)
    f.close()
