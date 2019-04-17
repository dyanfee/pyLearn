import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 模拟数据
n = 1000
# 随机均值为0 方差2 的数据
s1 = np.round(np.abs(np.random.normal(10, 3,  n)), decimals=1)
data = pd.DataFrame()
data['fir'] = s1
# print(data)
print(data['fir'].value_counts().sort_index())
fig, ax = plt.subplots()
ax.hist(data["fir"])  # 自动分跨度 频率柱状图
# ax, ylim(0, 10)# 设置y的取值区间
# ax.hist(data['fir'], bins=20)  # 分为20个跨度
# ax.hist(data['fir'], range(4, 5), bins=20) #取4到5之间的值分为20个跨度
plt.xlabel('Values')
plt.ylabel('Times')
plt.title('Plot')
plt.show()
