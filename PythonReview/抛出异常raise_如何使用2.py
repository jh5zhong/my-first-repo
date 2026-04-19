"""
在这个例子中，我们定义了一个名为validate_age的函数，该函数接受一个参数age，并检查其是否为负数或小于18岁。
如果条件满足，则使用raise语句引发一个ValueError异常，并传递一个错误消息。
在try-except块中，我们调用validate_age函数并捕获任何引发的异常。如果发生异常，则打印出错误消息
"""
def validate_age(age):  
    if age < 0:  
        raise Exception("年龄不能为负数")  #这里用Exception替换了ValueError
    elif age < 18:  
        raise Exception("年龄必须至少为18岁")  #这里用Exception替换了ValueError
    else:  
        return "年龄有效"  
  
try:
    input_number = int(input("请输入年龄："))
    result = validate_age(input_number)
    print(result)  
except Exception as e:  #这里用Exception替换了ValueError
    print("发生异常:", e)