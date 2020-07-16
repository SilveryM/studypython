import sys
import pygame
import time

import gamefunction as gf

from settings import Settings
from snake import Snake
from food import Food, FoodManager
from gamestats import Gamestats
from button import Button


def runGame():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screenWidth, settings.screenHegiht))
    pygame.display.set_caption(settings.gameName)

    interval = 1.0 / (settings.frame * 2)
    nextTime = time.time() + interval

    #创建开始按钮
    playButton = Button(settings, screen, "Play")

    gs = Gamestats(settings)
    
    #创建贪吃蛇
    snake = Snake(settings, screen)
    
    #食物管理器
    foodManager = FoodManager(settings, screen)

    while True:
        if time.time() < nextTime:
            continue
        nextTime = time.time() + interval

        gf.checkEvent(settings, screen, gs, snake, foodManager, playButton)

        #游戏进行中
        if gs.gameActive:
            snake.update()
            gf.updateFoods(settings, snake, foodManager)
        else:
            pass

        gf.updateScreen(settings, screen, gs, snake, foodManager, playButton)


if __name__ == "__main__":
    runGame()