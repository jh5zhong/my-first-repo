import math
input_pwrDbm = float(input("请输入功率值（单位dbm）："))
pwrW = math.pow(10, input_pwrDbm/10.0)/1000  # 转换公式W = pow(10, input_pwrDbm/10.0)/1000
pwrW = round(pwrW, 2)  # 保留两位小数
print(pwrW)
