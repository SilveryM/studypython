import sys
import pygame

def checkEvent(settings, snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake.direction != settings.Direction['Right']:
                    snake.direction = settings.Direction['Left']
            elif event.key == pygame.K_UP:
                if snake.direction != settings.Direction['Down']:
                    snake.direction = settings.Direction['Up']
            elif event.key == pygame.K_RIGHT:
                if snake.direction != settings.Direction['Left']:
                    snake.direction = settings.Direction['Right']
            elif event.key == pygame.K_DOWN:
                if snake.direction != settings.Direction['Up']:
                    snake.direction = settings.Direction['Down']


def updateScreen(settings, screen, snake):
    screen.fill(settings.bgColor)
    snake.blitme()
    pygame.display.flip()