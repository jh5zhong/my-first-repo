# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
a = power(5, 2)
b = power(5, 3)
c = power(5)   # 当第二个位置参数不写时，使用默认参数。即n = 2
print(a, b, c)
