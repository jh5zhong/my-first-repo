from datetime import datetime

dt = datetime.now()
print(dt)  # 2025-04-18 15:36:34.077123（微秒部分）


#去掉微秒
dt = datetime.now().replace(microsecond=0)
print(dt)  # 2025-04-18 15:36:34

#自定义格式化1
formatted = dt.strftime("%Y-%m-%d %H:%M:%S")  # 格式化为字符串
print(formatted)  # 2025-04-18 15:36:34

#自定义格式化2
formatted = dt.strftime("%d/%m/%Y")  # 格式化为字符串
print(formatted)

#自定义格式化3
formatted = dt.strftime("%A, %B %d")  # 格式化为字符串
print(formatted)
# 其他常见格式：
# "%d/%m/%Y" → 18/04/2025
# "%A, %B %d" → Friday, April 18

