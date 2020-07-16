import pygame
import random

from os import path
from pygame.sprite import Sprite
from pygame.sprite import Group


class FoodManager():
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.foodGroup = Group()

    def createFood(self):
        food = Food(self.settings, self.screen)
        self.foodGroup.add(food)
        return food


class Food(Sprite):
    def __init__(self, settings, screen):
        super(Food, self).__init__()

        self.settings = settings
        self.screen = screen

        spritesPath = path.dirname(__file__) + '/sprites/food.bmp'
        self.image = pygame.image.load(spritesPath)
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        widthNum = self.screenRect.width / self.settings.spriteSize
        heightNum = self.screenRect.height / self.settings.spriteSize

        self.rect.centerx = (random.random() * 10000 % widthNum) * self.settings.spriteSize
        self.rect.centery = (random.random() * 10000 % heightNum) * self.settings.spriteSize

    def blitme(self):
        self.screen.blit(self.image, self.rect)
