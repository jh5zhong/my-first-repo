# 用Python算两个列表相加
a = [1, 2, 3]
b = [4, 5, 6]
result1 = [x+y for x, y in zip(a, b)]  # 需要手动循环
print(result1)
# 用NumPy直接加
import numpy as np
result2 = np.array([1, 2, 3]) + np.array([4, 5, 6])  # 一行搞定

print(result2)
