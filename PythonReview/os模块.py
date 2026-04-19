#执行的结果相当于在windows的cmd窗口中输入ipconfig命令
import os
a = os.popen("ipconfig")
text = a.read()
print(text)

#执行的结果相当于在windows的cmd窗口中输入ping 10.227.93.28 -n 4命令
import os
a = os.popen("ping 10.227.127.11 -n 4")
text = a.read()
print(text)