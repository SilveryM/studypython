import pygame
from os import path
from settings import Settings


class Snake():
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        spritesPath = path.dirname(__file__) + '\sprites\head.bmp'
        self.image = pygame.image.load(spritesPath)
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery

        self.direction = self.settings.Direction['Left']

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.direction == self.settings.Direction['Left']:
            self.rect.centerx -= self.settings.speed
        elif self.direction == self.settings.Direction['Up']:
            self.rect.centery -= self.settings.speed
        elif self.direction == self.settings.Direction['Right']:
            self.rect.centerx += self.settings.speed
        elif self.direction == self.settings.Direction['Down']:
            self.rect.centery += self.settings.speed
            
    def addTail(self, foodGroup):
        food = foodGroup.sprites().pop()
        