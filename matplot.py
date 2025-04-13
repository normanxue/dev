import matplotlib.pyplot as plt
# modify by github web site
# 创建数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 17, 13]

# 绘制图形
plt.plot(x, y)

# 添加标题和标签
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图形
plt.show()
print("plt test success") 