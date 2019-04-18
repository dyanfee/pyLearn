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
print(y)
r = pd.value_counts(y)
# print(r)
data = pd.DataFrame(x, columns=["x"])
data["y"] = y
data["sex"] = sex
print(data)
# 两种方法生成 分类 如下图
# sns.stripplot(x="x", y="y", data=data, jitter=True)
sns.swarmplot(x="x", y="y", hue="sex", data=data)
plt.show()
