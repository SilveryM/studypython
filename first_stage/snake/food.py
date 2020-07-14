import pygame
import random

from os import path
from pygame.sprite import Sprite

class Food(Sprite):
    def __init__(self, settings, screen):
        super(Food, self).__init__()

        self.settings = settings
        self.screen = screen

        spritesPath = path.dirname(__file__) + '\sprites\head.bmp'
        self.image = pygame.image.load(spritesPath)
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        widthNum = self.screenRect.width
        heightNum = self.screenRect.height

        self.rect.centerx = random.random() * widthNum
        self.rect.centery = random.random() * heightNum

    def blitme(self):
        self.screen.blit(self.image, self.rect)
