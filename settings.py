# -*- coding: utf-8 -*-

#Author: Vaskka

class Settings():
    """游戏主要设置"""
    def __init__(self):
        '''各种游戏参数'''

        '''关于窗口'''
        self.win_width = 600
        self.win_height = 600

        '''关于背景'''
        self.background = 'images/background.bmp'

        '''关于长度和速度'''
        #游戏单位长度
        self.basic_side = 14
        #蛇的移动速度
        self.snack_speed = self.basic_side
        #单位蛇边长
        self.snack_per_side = self.basic_side
        #游戏速度
        self.speed = 0.1

        '''关于食物'''
        #食物的图像
        self.food_image = 'images/food.bmp'
        #食物的边长
        self.food_side = self.basic_side
        #吃下一块食物的分数
        self.food_done_score = 10

        '''关于蛇'''
        #蛇身体图像
        self.snack_per_image = 'images/snack_per_image.bmp'
        #蛇头图像
        self.snack_head_image_up = 'images/snack_head_image_up.bmp'
        self.snack_head_image_right = 'images/snack_head_image_right.bmp'
        self.snack_head_image_down = 'images/snack_head_image_down.bmp'
        self.snack_head_image_left = 'images/snack_head_image_left.bmp'

        #蛇内间距
        self.snack_per_padding = 2

        '''关于文字'''
        #文字字体
        self.font_style = None
        #文字颜色
        self.font_color = (0, 153, 51)
        #文字位置
        self.font_position = (20, 20)
        #开始游戏前引导文字的内容
        self.nav_font = 'Press SPACE to start the game!!'
        #开始游戏前引导文字的大小
        self.nav_font_size = 40
