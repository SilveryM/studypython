import sys
import pygame
from settings import Settings
from snake import Snake
import gamefunction as gf

def runGame():
    pygame.init()

    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHegiht))
    pygame.display.set_caption('TestGame')

    #创建贪吃蛇
    snake = Snake(aiSettings, screen)

    while True:
        gf.checkEvent(aiSettings, snake)
        snake.update()
        gf.updateScreen(aiSettings, screen, snake)

if __name__ == "__main__":
    runGame()