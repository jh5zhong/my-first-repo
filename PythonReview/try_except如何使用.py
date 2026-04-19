# 捕获指定异常，以下两个效果是一样的

# 一、捕获所有异常， 捕获异常描述信息
# try:
#     print(variable)
# except Exception as e:
#     print(e)

# 二、捕获指定异常， 捕获异常描述信息
# try:
#     print(variable)
# except NameError as e:
#     print(e)

# 二、捕获异常
try:
    print(variable)
except NameError:
    print("有错误")

