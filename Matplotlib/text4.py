import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 模拟数据
n = 100
# 随机均值为0 方差2 的数据
s1 = np.round(np.abs(np.random.normal(10, 3,  n)), decimals=1)
s2 = np.round(np.abs(np.random.normal(10, 3,  n)), decimals=1)
s3 = np.round(np.abs(np.random.normal(10, 3,  n)), decimals=1)
data = pd.DataFrame()
data['fir'] = s1
data['sec'] = s2
data['thi'] = s3
num_cols = ["fir", "sec", "thi"]
# print(data)
fig, ax = plt.subplots()
ax.boxplot(data[num_cols].values)
ax.set_xticklabels(num_cols) # x轴的名称
# ax.set_ylim(0, 10)  # 设置y的取值区间
plt.xlabel('Values')
plt.title('Plot')
plt.show()
