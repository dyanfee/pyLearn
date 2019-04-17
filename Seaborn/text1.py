import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def sinplot(flip=1):
    # 0到14之间取100个点
    x = np.linspace(0, 14, 100)
    style = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
    for j in range(5):
        plt.subplot(3, 2, j+1)
        for i in range(1, 7):
            plt.plot(x, np.sin(x+i*.5)*(7-i)*flip)
        sns.set_style(style[j])
        plt.title = style[j]


# 默认风格
# sns.set()
# 五种风格 darkgrid whitegrid dark white ticks
# sns.set_style('darkgrid')
# offset 到轴线的距离
# sns.despine(offset = 10)  # 去掉某些轴
sinplot()
plt.show()
