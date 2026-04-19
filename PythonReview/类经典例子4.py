"""
这个例子中，我们定义了一个名为Circle的类，它表示一个圆。
类中定义了两个方法area()和circumference()，分别用于计算圆的面积和周长。在__init__()方法中，我们初始化了一个表示半径的属性radius。
通过这个例子，你可以学习如何使用Python类来定义自己的数学对象，并为其实现所需的方法。这有助于加深对Python类和数学概念的理解。

"""

import math  
  
class Circle:  
    def __init__(self, radius):  
        self.radius = radius  
          
    def area(self):  
        return math.pi * self.radius ** 2  
      
    def circumference(self):  
        return 2 * math.pi * self.radius  
      
# 使用示例：  
circle = Circle(5)  
print("圆的面积：", circle.area())  # 输出：圆的面积： 78.53981633974483  
print("圆的周长：", circle.circumference())  # 输出：圆的周长： 31.41592653589793