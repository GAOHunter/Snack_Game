# -*- coding: utf-8 -*-

#Author: Vaskka
import pygame
import random
from pygame.sprite import Sprite

class Food(Sprite):
    """描述食物"""
    def __init__(self, screen, ai_settings):
        super(Food, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(self.ai_settings.food_image)
        self.rect = self.image.get_rect()

        #初始化位置
        self.rect.center = (20, 20)

    def blit_food(self):
        self.screen.blit(self.image, self.rect)
