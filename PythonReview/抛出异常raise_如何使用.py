"""
语法：raise 异常类对象
Exception是所有程序异常类的⽗类。
异常类对象为：Exception("错误提示信息")
"""
print("前面的代码已执行")
if True:
    raise Exception("变量未定义")
print("后面的代码为执行")