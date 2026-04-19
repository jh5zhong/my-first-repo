#self指的是调用该函数的对象，谁调用这个函数，self就是指谁。
#类：洗衣机，功能:洗衣服
class Washer():
    def wash(self):
        print('能洗衣服')
        print(self)
        
haier = Washer()#创建一个海尔洗衣机对象
print(haier) #打印海尔的内存地址

haier.wash()  #haier这个对象去调用wash这个函数
#由于打印对象和打印self得到的内存地址相同，所以self指的是调用该函数的对象

geli = Washer()
print(geli)
geli.wash()