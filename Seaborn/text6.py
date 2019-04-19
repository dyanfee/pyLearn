import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 生成300个数据
x = np.random.random_integers(0, 7, 300)
# 随机0,1
sex = np.random.randint(0, 2, 300)
# y = np.random.random(300)*10
y = np.abs(np.random.normal(0, 2, 300))
y2 = np.abs(np.random.normal(0, 2, 300))
# print(y)
data = pd.DataFrame(x, columns=["x"])
data["y"] = y
data["y2"] = y2
data["sex"] = sex

# g = sns.FacetGrid(data,col='sex')
# 条形图
# g.map(plt.hist,"y2")

# g = sns.FacetGrid(data, col="sex", hue='x')
# # 散点图
# g.map(plt.scatter, "y", "y2")
# # 添加说明项
# g.add_legend()
# palette 颜色字典
# hue_kws { market}
g = sns.FacetGrid(data, row="sex", margin_titles=True)
# 回归
# fit_reg 是否绘制回归的线
# row_order排序
# edgecolor 边缘颜色
# linewidth 线宽
# s 圆圈大小
# alpha 透明度
g.map(sns.regplot, "y2", "y", fit_reg=True)
# g.map(sns.barplot)
# 轴说明
# g.set_axis_labels = "name"
# 对轴的取值范围限定
g.set(xticks=[10, 20, 30], yticks=[10, 20, 30])

# 子图 wspace宽间距 hspace 高间距 
# 左右上下边距 left right bottom top
g.fig.subplots(wspace,hspace)
plt.show()
