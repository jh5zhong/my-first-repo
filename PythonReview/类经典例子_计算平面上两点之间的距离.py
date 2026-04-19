"""
这个例子中，我们定义了一个名为Point的类，它表示平面上的一个点。
类中定义了一个方法distance()，用于计算两点之间的距离。
该方法使用了平面几何中的勾股定理来计算两点之间的距离，并返回结果。通过这个例子，你可以学习如何使用Python类来定义自己的数学对象，并为其实现所需的方法。
这有助于加深对Python类和数学概念的理解。
在平面直角坐标系中,两点的坐标分别为(x1, y1)和(x2, y2)。那么这两点之间的距离公式可以表示为:d = √((x2 - x1)² + (y2 - y1)²)其中,d表示两点之间的距离。
"""

import math  
  
class Point:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
          
    def distance(self, other_point):  
        # 计算两点之间的距离  
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)  
        return distance          
      
# 使用示例：  
p1 = Point(1, 100)  
p2 = Point(4, 5)  
distance = p1.distance(p2)  #p2也是一个对象
#dis = "{:.2f}".format(distance)
print("两点之间的距离为：", "{:.2f}".format(distance))  # 输出：两点之间的距离为： 5.0