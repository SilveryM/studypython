import sys
import pygame


def checkGameOver(screen, snake, gs):
    screenRect = screen.get_rect()
    if snake.rect.left <= screenRect.left or snake.rect.right >= screenRect.right:
        gs.gameOver()


def checkEvent(settings, screen, snake, gs):
    if checkGameOver(screen, snake, gs):
        return

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


def updateFoods(settings, snake, foodGroup):
    if pygame.sprite.spritecollideany(snake, foodGroup):
        snake.addTail(foodGroup)


def updateScreen(settings, screen, snake, foodGroup):
    screen.fill(settings.bgColor)
    snake.blitme()
    foodGroup.draw(screen)
    pygame.display.flip()
