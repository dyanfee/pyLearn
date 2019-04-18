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
# 盒图 orient方向
# sns.boxplot(x="x", y="y2", data=data)
# 小提琴图
# sns.violinplot(x="x", y="y2", hue="sex", data=data, split=True, inner=None)
# sns.swarmplot(x="x", y="y2", data=data, color='w', alpha=0.5)
# 柱状图
# sns.barplot(x="sex", y="y2", hue="x", data=data)

# 点图
# sns.pointplot(x="sex", y="y2", hue="x", data=data,
#                 palette={"0": "g", "1": "m"},
#                 markers=["^", "o"], linestyles=["-", "--"])

# 任意图 kind类型 "bar" "swarm" "box" ---
# sns.factorplot(x="sex", y="y2", hue="x", data=data,kind="bar")
plt.show()
