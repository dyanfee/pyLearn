import matplotlib.pyplot as plt
from PIL import Image
import os
import json
import time

# 图片所在文件夹
imgDir = r'E:\WorkSpace\parkingPos'
outFileName = os.path.join(imgDir, 'posInfo_' + time.strftime('%Y-%m-%d-%H-%M'))
supportImgType = ['jpg', 'png']
scale = 0.66

def getPos(f):
    im = Image.open(os.path.join(imgDir, f))
    plt.imshow(im)
    # 默认最多30个点，等待时间默认120秒，描绘完enter结束
    pos = plt.ginput(30, timeout=120)
    plt.close()
    print(pos)
    return pos, im.size


def main():
    # imgFiles = os.listdir(imgDir)
    posDict = {}
    posArray = {}
    for f in os.listdir(imgDir):
        if f.split('.')[-1] not in supportImgType:
            continue

        print('开始描绘: '+f)
        name = f.split('.')[0]
        while True:
            positions, size = getPos(f)
            command = input('y:保存\nn:放弃\nother:重来\n请选择：')
            if command == 'y':
                # 字典格式保存
                posDict[name] = positions
                # 一维数组格式保存
                posList = []
                # posList.extend(size)
                for p in positions:
                    posList.extend(p)
                posList = [int(i*scale) for i in posList]
                posArray[name] = posList
                break

            if command == 'n':
                break

    print('done')
    print(posArray)
    print(posDict)

    jsonStr = json.dumps(posDict)
    with open(outFileName+'.json', 'w', encoding='utf-8') as jsonFile:
        jsonFile.write(jsonStr)
    with open(outFileName+'.txt', 'w', encoding='utf-8') as infoFile:
        nameList = []
        for f in posArray:
            nameList.append(f)
            infoFile.write(f + ': ' + str(posArray[f])+',\n')
        # infoFile.write(str(nameList))


if __name__ == '__main__':
    input_scale = input("输入缩放比例(默认0.66)：")
    if input_scale != "":
        scale = input_scale
    main()
