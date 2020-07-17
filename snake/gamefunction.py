import sys
import pygame


def checkGameOver(screen, snake, gs):
    screenRect = screen.get_rect()
    if snake.rect.left <= screenRect.left or snake.rect.right >= screenRect.right or snake.rect.top <= screenRect.top or snake.rect.bottom >= screenRect.bottom:
        gs.gameOver()
        pygame.mouse.set_visible(True)


def checkEvent(settings, screen, gs, snake, foodManager, playButton):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            checkPlayButton(settings, screen, gs, snake, foodManager,
                            playButton, mouseX, mouseY)


def checkPlayButton(settings, screen, gs, snake, foodManager, playButton,
                    mouseX, mouseY):
    buttonClick = playButton.rect.collidepoint(mouseX, mouseY)
    if buttonClick and not gs.gameActive:
        pygame.mouse.set_visible(False)
        gs.resetStats()

        snake.Reset()
        foodManager.Reset()


def updateFoods(settings, snake, foodManager):
    foodGroup = foodManager.foodGroup
    if pygame.sprite.spritecollideany(snake, foodGroup):
        snake.addTail(foodGroup)
        pygame.sprite.spritecollide(snake, foodGroup, True)

        foodManager.clearFood()
        foodManager.createFood()


def updateScreen(settings, screen, gs, snake, foodManager, playButton):
    screen.fill(settings.bgColor)
    snake.blitme()
    foodManager.foodGroup.draw(screen)

    if not gs.gameActive:
        playButton.drawButton()

    pygame.display.flip()