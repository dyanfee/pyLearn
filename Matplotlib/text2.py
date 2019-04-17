import matplotlib.pyplot as plt
import numpy as np

# 模拟数据
n = 500
# 随机均值为0 方差2 的数据
s1 = np.random.normal(0, 2, n)
s2 = np.random.normal(3, 5, n)
print(type(s1))

fig, ax = plt.subplots()
ax.scatter(s1, s2)  # 绘制散点图
plt.xlabel('s1')
plt.ylabel('s2')
plt.title('Scatter plot')
plt.show()
