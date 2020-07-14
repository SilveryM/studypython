import pygame
from os import path
from settings import Settings


class Snake():
    def __init__(self, aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen

        spritesPath = path.dirname(__file__) + '\sprites\head.bmp'
        self.image = pygame.image.load(spritesPath)
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery

        self.direction = self.aiSettings.Direction['Left']

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.direction == self.aiSettings.Direction['Left']:
            self.rect.centerx -= self.aiSettings.speed
        elif self.direction == self.aiSettings.Direction['Up']:
            self.rect.centery -= self.aiSettings.speed
        elif self.direction == self.aiSettings.Direction['Right']:
            self.rect.centerx += self.aiSettings.speed
        elif self.direction == self.aiSettings.Direction['Down']:
            self.rect.centery += self.aiSettings.speed