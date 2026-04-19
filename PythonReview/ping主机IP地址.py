import os
import time
# cIp = '10.227.93.27'
# tIp = '10.227.93.28'
os.system('ping -s 1000 -c 5 10.227.252.32')  #ping4个包

#或者下面这个，没有乱码，不错！
time.sleep(6)  #延时10秒
a = os.popen('ping -s 1000 -c 5 10.227.252.33')#没有过程，可以直接打印结果出来
text = a.read()
print(text)


