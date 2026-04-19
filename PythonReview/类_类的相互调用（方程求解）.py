
'''
一元二次方程ax2+bx+c=0的求解是常见的数学问题，而在a=0时，一元二次方程的求解转化为一元一次方程的求解。下面利用面向对象的思想编写两个类，分别
用于根据系数求相应一元一次方程或一元二次方程的解。
'''

from math import sqrt  #导入math模块，为使用sqrt函数做准备
class Linear(object):#定义一元一次方程类
    def __init__(self,a,b):#定义类的构造方法
        self.a = a
        self.b = b
    def Solver(self):#定义实例方法，求一元一次方程的解
        if self.a != 0:
            return "此一元一次方程有唯一解："+str(-self.b/self.a)
        elif self.b == 0:
            return "此一元一次方程有无数解"
        else:
            return "此一元一次方程无解"
class Quadratic(object):#定义一元二次方程类
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def Solver(self):
        if self.a == 0:
            obj = Linear(self.b,self.c)
            return obj.Solver()
        else:#如果a不等于0，则按照一元二次方程求解
            delta = self.b**2 - 4*self.a*self.c
            if delta >= 0:
                x1 = (-self.b+sqrt(delta))/(2*self.a)
                x2 = (-self.b-sqrt(delta))/(2*self.a)
                return "此一元二次方程有两个实数解："+str(x1)+','+str(x2)
            else:
                return "此一元二次方程无实数解"
formula1 = Quadratic(0,0,1)#1=0
formula2 = Quadratic(3,4,5)#3X2+4X+5 = 0
formula3 = Quadratic(1,2,-3)
formula4 = Quadratic(0,3,1)
formula5 = Quadratic(0,0,0)
print(formula1.Solver())
print(formula2.Solver())
print(formula3.Solver())
print(formula4.Solver())
print(formula5.Solver())
                

        