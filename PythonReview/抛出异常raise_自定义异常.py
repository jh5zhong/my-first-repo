'''
因为错误是class，捕获一个错误就是捕获到该class的一个实例(异常对象)。因此，错误并不是凭空产生的，而是有意创建并抛出的。
python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例。
'''
apple = int(input("请输入苹果的个数：")) # 输入苹果的数量
children = int(input("请输入来了几个小朋友："))
if apple < children:
    raise ValueError("苹果太少了，不够分……")
    #raise Exception("苹果太少了，不够分……")  #NameError(python存在的异常名字，一般选和报错信息相似的,这里换成Exception),是Python内置的，引号里面的内容可以自己写
if apple > children:
    print('可以正常分苹果')

