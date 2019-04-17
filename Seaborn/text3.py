import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 自带数据集
# iris = sns.load_dataset("tips")
# iris.head()
mean, cov = [0, 1], [(1, 0.5), (.5, 1)]
# 生成200个数据 两组
data = np.random.multivariate_normal(mean, cov, 200)

data = pd.DataFrame(data, columns=["x", "y"])
print(data)

sns.regplot(x="x", y="y", data = data)
plt.show()
