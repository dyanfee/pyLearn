import matplotlib.pyplot as plt
import pandas as pd
from numpy import arange

# data = pd.DataFrame({'Name':[4,4.5,4.3,3,3.7]})
# 模拟数据
data = pd.DataFrame({'First':[3],'Second':[4.5],'Third':[3.4],'Fourth':[4.4],'Fifth':[4.3]})
# 列名
num_cols = ['First','Second','Third','Fourth','Fifth']
print(data)
bar_heights = data.ix[0,num_cols].values
print(bar_heights)
bar_positions = arange(5) + 0.5 
print(bar_positions)
fig,ax = plt.subplots()
# 设置X的位置和y值高度 和列宽度
ax.bar(bar_positions,bar_heights,0.4)
# ax.barh(bar_positions,bar_heights,0.4) #绘制横向的图
# ax.scatter(series,series) #绘制散点图
plt.show()