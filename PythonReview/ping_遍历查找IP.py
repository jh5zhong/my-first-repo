# import os
# for i in range(1,255):
#     ip = '192.{}.1.16'.format(i)
#     #print(ip)
#     os.system('ping {} -n 4'.format(ip))



import os
for i in range(1,255):
    ip = '192.168.1.{}'.format(i)
    #print(ip)
    os.system('ping {} -n 4'.format(ip))

