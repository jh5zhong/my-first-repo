# -*- coding: UTF-8 -*-

import os
def main():
    print('Hello world')
    print("这是Alcie\'的问候。")
    print('这是Bob\'的问候。')
    foo(2,24)
    print('=' * 10)
    print('这个将直接执行' + os.getcwd())
    counter = 0
    counter += 1
    food = ['苹果','杏子','李子','梨']
    for i in food:
        print('俺就爱整只:' + i)
    print('数到10')
    for i in range(10):
        print(i)

def foo(paraml,secondParam):
    res = paraml + secondParam
    print('%s 加 %s 等于 %s' % (paraml,secondParam,res))
    if res < 50:
        print('这个')
    elif (res >= 50) and ((paraml == 42) or (secondParam == 24)):
        print('那个')
    else:
        print('嗯')
    return res
if __name__ == '__main__':
    main()