import sys
import pygame
import time

import gamefunction as gf

from settings import Settings
from snake import Snake
from food import Food
from gamestats import Gamestats
from pygame.sprite import Group


def runGame():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screenWidth, settings.screenHegiht))
    pygame.display.set_caption('TestGame')

    interval = 1.0 / 30
    nextTime = time.time() + interval

    #创建贪吃蛇
    gs = Gamestats(settings)
    snake = Snake(settings, screen)

    foodGroup = Group()
    food = Food(settings, screen)
    foodGroup.add(food)

    while True:
        if time.time() < nextTime:
            continue
        nextTime = time.time() + interval

        gf.checkEvent(settings, screen, snake, gs)
        
        #游戏进行中
        if gs.gameActive:
            snake.update()
            gf.updateFoods(settings, snake, foodGroup)
        
        gf.updateScreen(settings, screen, snake, foodGroup)


if __name__ == "__main__":
    runGame()