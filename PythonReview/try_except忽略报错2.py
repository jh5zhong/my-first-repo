#尝试以 r 模式打开⽂件，如果⽂件不存在，则以 w ⽅式打开。

try:
 f = open('test.txt', 'r')
except:
 f = open('test.txt', 'w')