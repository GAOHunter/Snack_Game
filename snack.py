# -*- coding: utf-8 -*-

#Author: Vaskka
import copy
import pygame
import pygame.sprite
from snack_per import snack_per
from pygame.sprite import Sprite


class Snack():
    """描述蛇"""
    def __init__(self, screen, ai_settings):
        '''描述蛇的属性'''
        self.ai_settings = ai_settings
        self.screen = screen
        #初始化单位蛇的列表
        self.snack_list = []

        for i in range(5):
            snk_per = snack_per(screen, ai_settings)
            self.snack_list.append(snk_per)
        #记录列表中单位蛇的数目
        self.count = len(self.snack_list)
        #初始化全部单位蛇的部分属性和位置
        self.init_all_snack_index()
        self.init_all_snack_position()
        
    def init_all_snack_index(self):
        '''初始化整条蛇中全部单位蛇的"上一个单位蛇"属性以及蛇头的"下一个单位蛇"属性'''
        for i in range(self.count - 1):
            self.snack_list[i + 1].front_snack_per_rect = copy.deepcopy(self.snack_list[i].rect)
        #设置蛇头属性
        self.snack_list[0].is_head = True
        self.snack_list[0].next_snack_per = self.snack_list[1]

    def init_all_snack_position(self):
        '''初始化全部单位蛇的位置'''
        i = 1
        for snk in self.snack_list:
            if snk.is_head:
                continue
            else:
                snk.rect.y += (self.ai_settings.snack_per_side + self.ai_settings.snack_per_padding) * i
                i += 1

    def add_a_snack_per(self, screen):
        '''向单位蛇列表中添加一个单位蛇'''
        #创建一个新单位蛇
        new_snack_per = snack_per(screen, self.ai_settings)
        #调整新单位蛇的属性
        new_snack_per.front_snack_per_rect = copy.deepcopy(self.snack_list[self.count - 1].rect)
        new_snack_per.moving_dorection = self.snack_list[self.count - 1].moving_direction

        #添加到列表中, 并且将总数 + 1
        self.snack_list.append(new_snack_per)
        self.count += 1

    def update_snack(self, ai_settings):
        '''更新整条蛇的位置'''
        for snk in self.snack_list:
            snk.update(ai_settings)
        #更新所有单位蛇的上一个矩形对象
        for i in range(self.count - 1):
            self.snack_list[i + 1].front_snack_per_rect = copy.deepcopy(self.snack_list[i].rect)

    def blit_snack(self):
        '''显示整条蛇'''
        for snk in self.snack_list:
            snk.snack_per_blit()

    def check_move_request(self, direction, ai_settings, snack):
        '''检查移动操作是否合理'''

        if direction == 1:
            if snack.snack_list[0].moving_direction == 3:
                return False
            else:
                return True
        elif direction == 2:
            if snack.snack_list[0].moving_direction == 4:
                return False
            else:
                return True
        elif direction == 3:
            if snack.snack_list[0].moving_direction == 1:
                return False
            else:
                return True
        elif direction == 4:
            if snack.snack_list[0].moving_direction == 2:
                return False
            else:
                return True
        else:
            return True

    def check_over(self, ai_settings):
        '''检查是否接触屏幕边缘及自身'''
        if self.snack_list[0].rect.top < 0:
            return False
        elif self.snack_list[0].rect.right > ai_settings.win_width:
            return False
        elif self.snack_list[0].rect.bottom > ai_settings.win_height:
            return False
        elif self.snack_list[0].rect.left < 0:
            return False
        elif self.check_collide_self():
            return False
        else:
            return True

    def check_collide_self(self):
        '''检查自身碰撞'''
        for i in range(1, self.count):
            if pygame.sprite.collide_rect(self.snack_list[0], self.snack_list[i]):
                return True
        return False

    def reset_snack(self):
        self.snack_list = []

        for i in range(5):
            snk_per = snack_per(self.screen, self.ai_settings)
            self.snack_list.append(snk_per)
        #记录列表中单位蛇的数目
        self.count = len(self.snack_list)
        #初始化全部单位蛇的部分属性和位置
        self.init_all_snack_index()
        self.init_all_snack_position()
