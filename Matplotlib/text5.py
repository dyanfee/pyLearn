import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 模拟数据
n = 10
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

# fig=plt.figure(figsize=(3,3))
# ax = fig.add_subplot(1,1,1)

fig, ax = plt.subplots()
# c 指定颜色 linewidth指定线条宽度
ax.plot(data["fir"], label='First', c=(0/255, 0/255, 0/255), linewidth=3)
ax.plot(data['sec'], label='Sceond')
ax.plot(data['thi'], label='Third')
plt.xlabel('Values')
plt.title('Plot')
ax.legend(loc='upper right')
plt.savefig('./Matplotlib/plt.png')
plt.show()
