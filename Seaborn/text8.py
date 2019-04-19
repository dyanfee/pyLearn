import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# randn 有正负
data = np.random.randn(3, 3)
# data = np.random.rand(3, 3)
# data = np.random.rand(100, 100)
# 热度图
# vmin 最小取值 vmax最大取值
# center 中心值
# annot 显示值 fmt 字符格式
# linewidth 间距
# cmap 调色板 YlGnBu 蓝色
# cbar 是否掩藏 colorbar
hetmap = sns.heatmap(data, vmin=0.2, vmax=0.3, center=0, annot=True)
plt.show()
