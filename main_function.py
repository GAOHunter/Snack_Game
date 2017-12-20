# -*- coding: utf-8 -*-

#Author: Vaskka
import random
import pygame
import pygame.sprite
import pygame.font
from food import Food
from snack import Snack

def check_event(status, snack, ai_settings):
    '''处理事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            handle_keydown_event(event, status, snack, ai_settings)
        elif event.type == pygame.KEYUP:
            handle_keyup_event(event)

def handle_keydown_event(event, status, snack, ai_settings):
    '''处理按键事件'''
    if event.key == pygame.K_UP and status.activity == True and snack.check_move_request(1, ai_settings, snack):
        snack.snack_list[0].moving_direction = 1
    elif event.key == pygame.K_RIGHT and status.activity == True and snack.check_move_request(2, ai_settings, snack):
        snack.snack_list[0].moving_direction = 2
    elif event.key == pygame.K_DOWN and status.activity == True and snack.check_move_request(3, ai_settings, snack):
        snack.snack_list[0].moving_direction = 3
    elif event.key == pygame.K_LEFT and status.activity == True and snack.check_move_request(4, ai_settings, snack):
        snack.snack_list[0].moving_direction = 4
    elif event.key == pygame.K_SPACE and status.activity == False:
        status.activity = True

def handle_keyup_event(event):
    '''处理放键事件'''
    pass

def snack_update(snack, ai_settings, foods, screen, status):
    '''更新蛇'''
    for fd in foods.copy():
        if pygame.sprite.collide_rect(fd, snack.snack_list[0]):
            status.score += ai_settings.food_done_score
            foods.remove(fd)
            snack.add_a_snack_per(screen)

    if snack.check_over(ai_settings):
        snack.update_snack(ai_settings)
        snack.blit_snack()
    else:
        restart(status, foods, snack, screen, ai_settings)

def food_update(snack, ai_settings, screen, foods):
    '''更新食物'''
    if len(foods) == 0:
        #记录是否发生碰撞
        is_collide = False

        #构造新食物
        new_food = Food(screen, ai_settings)

        test_rect = new_food.rect.copy()
        while True:
            #构造随机位置
            test_rect.centerx = random.randint(ai_settings.food_side, ai_settings.win_width - ai_settings.food_side)
            test_rect.centery = random.randint(ai_settings.food_side, ai_settings.win_height - ai_settings.food_side)

            #检查碰撞
            for snk in snack.snack_list:
                if pygame.Rect.colliderect(test_rect, snk.rect):
                    is_collide = True
                    break

            if is_collide == False:
                new_food.rect = test_rect
                foods.append(new_food)
                new_food.blit_food()
                break
            else:
                is_collide = False
    else:
        for fd in foods:
            fd.blit_food()

def score_update(status, screen, font, ai_settings):
    '''更新分数'''
    score_surface = font.render('Score: ' + str(status.score), True, ai_settings.font_color)  
    screen.blit(score_surface, ai_settings.font_position)


def screen_update(screen, ai_settings):
    '''更新背景'''
    screen.blit(pygame.image.load(ai_settings.background), (0, 0))

def nav_font_update(screen, font, ai_settings):
    '''更新游戏前的引导文字'''
    font = pygame.font.SysFont(ai_settings.font_style, ai_settings.nav_font_size)
    nav_font_surface = font.render(ai_settings.nav_font, True, ai_settings.font_color)
    screen.blit(nav_font_surface, (2 * ai_settings.nav_font_size, ai_settings.win_height / 2))

def restart(status, foods, snack, screen, ai_settings):
    snack.reset_snack()
    foods = []
    status.activity = False
    status.score = 0
