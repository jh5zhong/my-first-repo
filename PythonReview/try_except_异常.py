'''
异常发生的情况
1、程序编写的问题
2、用户输入的问题
3、外在因素条件
其中 ZeroDivisionError 是个异常对象。Python 在无法按你的要求做时，就会创建这种对象。
在这种情况下，Python 将停止运行程序，并指出引发了哪种异常，而我们可根据这些信息对程序进行修改来修正代码。
'''
#尝试执行导入模块，捕获Exception 打印异常描述信息
try:
    import pandas
except Exception as pd:
    print(pd)
#直接忽略错误
try:
    import pandas
except:
    pass
#捕获指定异常
try:
    import pandas
except ModuleNotFoundError:#如果捕获到的这个异常类型不正常，后面的print语句不会被执行
    print('有错误')
    
#捕获多个指定异常
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('0不能被整除')
#自定义异常
try:
    print(1/0)
except:
    raise Exception("0不能被1整除")

