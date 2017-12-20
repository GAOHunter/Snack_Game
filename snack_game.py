# -*- coding: utf-8 -*-

#Author: Vaskka
import time
import pygame
import pygame.font
from settings import Settings
from status import Status
from snack import Snack
import main_function as f

def main():
    #初始化pygame
    pygame.init()
    #初始化游戏设置
    ai_settings = Settings()
    #初始化游戏状态
    status = Status()

    #初始化屏幕
    screen = pygame.display.set_mode((ai_settings.win_width, ai_settings.win_height))
    #初始化一条蛇
    snack = Snack(screen, ai_settings)
    #初始化食物列表
    foods = []
    #初始化字体
    font = pygame.font.SysFont(ai_settings.font_style, 25)

    #游戏主循环
    while True:
        #监视事件
        f.check_event(status, snack, ai_settings)
        f.screen_update(screen, ai_settings)
        if status.activity:
            f.snack_update(snack, ai_settings, foods, screen, status)
            f.food_update(snack, ai_settings, screen, foods)
            f.score_update(status, screen, font, ai_settings)
            time.sleep(ai_settings.speed)
        else:
            f.nav_font_update(screen, font, ai_settings)
        pygame.display.update()



if __name__ == '__main__':
    main()

