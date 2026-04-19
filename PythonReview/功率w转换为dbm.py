import math
input_pwrW = float(input("请输入功率值（单位W）："))
pwrDbm = 10*math.log10(input_pwrW*1000)  # 转换公式dBm = 10 * log10(功率值(mW))
pwrDbm = round(pwrDbm, 2)  # 保留两位小数
print(pwrDbm)
