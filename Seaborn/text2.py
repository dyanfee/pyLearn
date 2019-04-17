import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mean, cov = [0, 1], [(1, 0.5), (.5, 1)]
# 生成200个数据 两组
data = np.random.multivariate_normal(mean, cov, 200)

data = pd.DataFrame(data, columns=["x", "y"])
print(data)

# sns.jointplot(x="x", y="y", data=data)
# kind 指定点的样式 hex六边形
sns.jointplot(x="x", y="y",kind="hex", data=data,color=sns.palplot(sns.light_palette("green")))
plt.show()