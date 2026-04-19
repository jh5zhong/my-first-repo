"""
这个例子中，我们定义了一个名为QuadraticEquation的类，它接受三个参数：a、b和c，分别代表一元二次方程的系数。
类中定义了一个方法calculate_root()，用于计算一元二次方程的根。
根据判别式的值，我们使用不同的算法来计算根，并返回两个值：实根1和实根2。如果判别式小于0，则返回None表示无实根。
"""
import math  
  
class QuadraticEquation:  
    def __init__(self, a, b, c):  
        self.a = a  
        self.b = b  
        self.c = c  
          
    def calculate_root(self):  
        # 计算判别式  
        delta = self.b**2 - 4*self.a*self.c  
          
        # 判别式小于0，无实根  
        if delta < 0:  
            return None, None  
          
        # 判别式等于0，有一个实根  
        if delta == 0:  
            root = -self.b / (2*self.a)  
            return root, None  
          
        # 判别式大于0，有两个实根  
        if delta > 0:  
            root1 = (-self.b + math.sqrt(delta)) / (2*self.a)  
            root2 = (-self.b - math.sqrt(delta)) / (2*self.a)  
            return root1, root2  
      
# 使用示例：  
equation = QuadraticEquation(1, -3, 2)  # a=1, b=-3, c=2  
root1, root2 = equation.calculate_root() 
root3 = "{:.2f}".format(root1) #保留两位小数
root4 = "{:.2f}".format(root2) #保留两位小数
print("Roots are {} and {}".format(root1,root2))# Output: Roots are -1.0 and -2.0
print("Roots are {} and {}".format(root3,root4))  # Output: Roots are -1.0 and -2.0