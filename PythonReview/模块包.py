import sys
print(sys.path)

# 1. 导入模块
from classic.mypackage.my_module02 import add


# 2. 调用功能
add(3, 6)


# 1. import 包名.模块名
#import classic.mypackage.my_module03
from classic.mypackage import my_module03
# 2. 调用功能
my_module03.chengfa(3, 6)