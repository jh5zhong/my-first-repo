import pygame
import sys
#初始化pygame
pygame.init()

screen = pygame.display.set_mode((320,240)) #设置窗口

while True:
    #添加检测事件
    for event in pygame.event.get(): # 获取所有事件
        if event.type == pygame.QUIT:
            sys.exit()
pygame.quit()#退出游戏