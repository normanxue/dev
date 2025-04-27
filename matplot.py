import matplotlib.pyplot as plt
import numpy as np
# modify by github web site
# 创建数据
x = np.array(range(0,10,1))
y = np.array(range(40,80,4))

# 绘制图形
plt.plot(x, y)

# 添加标题和标签
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图形
plt.show()
print("plt test success") 