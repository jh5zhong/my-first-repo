"""
这个例子中，我们定义了一个名为QuadraticEquation的类，它表示一元二次方程。
类中定义了一个方法solve()，用于求解一元二次方程。该方法首先计算判别式的值，然后根据判别式的值判断方程的解的情况，并返回相应的结果。
通过这个例子，你可以学习如何使用Python类来定义自己的数学对象，并为其实现所需的方法。
这有助于加深对Python类和数学概念的理解。

"""
import math
class QuadraticEquation:  
    def __init__(self, a, b, c):  
        self.a = a  
        self.b = b  
        self.c = c  
          
    def solve(self):  
        # 计算判别式  
        discriminant = self.b ** 2 - 4 * self.a * self.c  
          
        # 判断判别式的值  
        if discriminant < 0:  
            return "无实数解"  
        elif discriminant == 0:  
            sol = -self.b / (2 * self.a)  
            return "有一个实数解：{}".format(sol) 
        else:  
            sol1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)  
            sol2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)  
            return "有两个实数解：{} 和 {}".format(sol1,sol2)  
      
# 使用示例：  
equation = QuadraticEquation(2, -3, 1)  
result = equation.solve()  
print(result)  # 输出：有两个实数解：1.5 和 -0.5
print("----------------------------")
# 使用示例：  
equation = QuadraticEquation(4, 5, 3)  
result = equation.solve()  
print(result)  # 输出：有两个实数解：1.5 和 -0.5
print("----------------------------")
equation = QuadraticEquation(3, -6, 3)  
result = equation.solve()  
print(result)  # 输出：有两个实数解：1.5 和 -0.5
print("----------------------------")