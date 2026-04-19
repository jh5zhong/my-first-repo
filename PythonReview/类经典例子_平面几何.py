"""
这个例子中，我们定义了三个类：Point、Segment和Triangle。
Point类表示平面上的一个点，Segment类表示连接两个点的线段，Triangle类表示由三条线段构成的三角形。
每个类都有一些方法，用于计算点之间的距离、线段的长度和三角形的周长和面积。
通过这个例子，你可以学习如何使用Python类来定义自己的数学对象，并为其实现所需的方法。这有助于加深对Python类和数学概念的理解。
三角形面积：S= √[p(p-a)(p-b)(p-c)]；其中：p=(a+b+c)/2 ；
"""

import math  
  
class Point:  #入参为x和y两个数字
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
          
    def distance(self, other_point):  
        # 计算两点之间的距离  
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)  
        return distance  
      
class Segment:  #入参为Point实例化后的两个对象
    def __init__(self, start_point, end_point):  
        self.start = start_point  
        self.end = end_point  
          
    def length(self):  
        # 计算线段的长度  
        length = self.start.distance(self.end)  
        return length  
      
class Triangle:  #入参为Point实例化后的3个对象
    def __init__(self, point1, point2, point3):  
        self.a = Segment(point1, point2)  
        self.b = Segment(point2, point3)  
        self.c = Segment(point3, point1)  
          
    def perimeter(self):  
        # 计算三角形的周长  
        perimeter = self.a.length() + self.b.length() + self.c.length()  
        return perimeter  
      
    def area(self):  
        # 计算三角形的面积，使用海伦公式  
        s = (self.a.length() + self.b.length() + self.c.length()) / 2  
        area = math.sqrt(s * (s - self.a.length()) * (s - self.b.length()) * (s - self.c.length()))  
        return area  
      
# 使用示例：  
p1 = Point(0, 0)  
p2 = Point(4, 0)  
p3 = Point(0, 3)  
t1 = Triangle(p1, p2, p3)  
print("三角形的周长为：", t1.perimeter())  # 输出：三角形的周长为： 12.0  
print("三角形的面积为：", t1.area())  # 输出：三角形的面积为： 6.0