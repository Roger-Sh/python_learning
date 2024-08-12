import numpy as np

# 创建一个 2D 数组
arr = np.array([[1, 5, 2], [4, 3, 6]])

# 获取数组中的最大值
max_value = np.max(arr)
print("最大值:", max_value)  # 输出: 最大值: 6

# 获取最大值的位置索引
max_index = np.argmax(arr)
print("最大值的索引:", max_index)  # 输出: 最大值的索引: 5

# 如果需要获取 2D 数组中最大值的行列索引
row_index, col_index = np.unravel_index(max_index, arr.shape)
print("最大值的行列索引:", row_index, col_index)  # 输出: 最大值的行列索引: 1 2

