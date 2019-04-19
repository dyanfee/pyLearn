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
# 两两绘制图
# vars 指定绘制的数据
# palette 调色
g = sns.PairGrid(data,vars=["y","y2"])
# 对角线绘制图的类型
g.map_diag(plt.hist)
# 非对角线 绘制图的类型
g.map_offdiag(plt.scatter)

g.map(data)

plt.show()
