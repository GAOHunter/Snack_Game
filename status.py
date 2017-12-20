# -*- coding: utf-8 -*-

#Author: Vaskka

class Status():
    """描述游戏状态"""
    def __init__(self):
        #游戏是否开始
        self.activity = False
        #游戏得分
        self.score = 0

    def add_score(self, ai_settings):
        self.score += ai_settings.food_done_score
        
