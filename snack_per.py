# -*- coding: utf-8 -*-

#Author: Vaskka

import pygame
from pygame.sprite import Sprite

class snack_per(Sprite):
    """描述单位蛇"""
    def __init__(self, screen, ai_settings):
        super(snack_per, self).__init__()
        '''单位蛇的基本属性'''
        #是否是蛇头
        self.is_head = False
        #正在移动的方向(1: 上, 2: 右, 3: 下, 4: 左)
        self.moving_direction = 2
        #上一个单位蛇
        self.front_snack_per_rect = None
        #(蛇头专属)下一个单位蛇(用来判断当前移动命令是否有效)
        self.next_snack_per = None
        '''单位蛇的图像属性'''
        self.screen = screen
        self.body_image = pygame.image.load(ai_settings.snack_per_image)
        self.head_image_up = pygame.image.load(ai_settings.snack_head_image_up)
        self.head_image_right = pygame.image.load(ai_settings.snack_head_image_right)
        self.head_image_down = pygame.image.load(ai_settings.snack_head_image_down)
        self.head_image_left = pygame.image.load(ai_settings.snack_head_image_left)
        self.rect = self.body_image.get_rect()
        self.rect.center = self.screen.get_rect().center

    def set_snack_head(self):
        '''设置为蛇头'''
        self.rect = head_image.get_rect()
        self.rect.center = self.screen.center

    def update(self, ai_settings):
        #蛇的速度和内边距
        speed = ai_settings.snack_speed
        padding = ai_settings.snack_per_padding

        if self.is_head:
            if self.moving_direction == 1:
                self.rect = self.rect.move(0, -(speed + padding))
                return
            elif self.moving_direction == 2:
                self.rect = self.rect.move(speed + padding, 0)
                return
            elif self.moving_direction == 3:
                self.rect = self.rect.move(0, speed + padding)
                return
            elif self.moving_direction == 4:
                self.rect = self.rect.move(-(speed + padding), 0)
                return
        else:
            self.rect.center = self.front_snack_per_rect.center

    def snack_per_blit(self):
        '''显示每个单位蛇到屏幕'''
        if self.is_head:
            if self.moving_direction == 1:
                self.screen.blit(self.head_image_up, self.rect)              
            elif self.moving_direction == 2:
                self.screen.blit(self.head_image_right, self.rect)
            elif self.moving_direction == 3:
                self.screen.blit(self.head_image_down, self.rect)
            elif self.moving_direction == 4:
                self.screen.blit(self.head_image_left, self.rect)
        else:
            self.screen.blit(self.body_image, self.rect)

