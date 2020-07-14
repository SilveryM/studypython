import sys
import pygame
import time
from settings import Settings
from snake import Snake
import gamefunction as gf


def runGame():
    pygame.init()

    aiSettings = Settings()
    screen = pygame.display.set_mode(
        (aiSettings.screenWidth, aiSettings.screenHegiht))
    pygame.display.set_caption('TestGame')

    interval = 1.0 / 30
    nextTime = time.time() + interval

    #创建贪吃蛇
    snake = Snake(aiSettings, screen)

    while True:
        if time.time() < nextTime:
            continue
        nextTime = time.time() + interval

        gf.checkEvent(aiSettings, screen, snake)
        snake.update()
        gf.updateScreen(aiSettings, screen, snake)


if __name__ == "__main__":
    runGame()