import pygame
from os import path
from settings import Settings


class Snake():
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        spritesPath = path.dirname(__file__) + '/sprites/head.bmp'
        image = pygame.image.load(spritesPath)
        self.rect = image.get_rect()
        self.screenRect = self.screen.get_rect()

        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery

        self.direction = self.settings.Direction['Left']

        #身体关节列表
        self.imageList = []
        self.imageList.append([image, self.rect])

    def blitme(self):
        for i in self.imageList:
            [image, rect] = i
            self.screen.blit(image, rect)

    def update(self):
        nextCenterX = 0
        nextCenterY = 0
        if self.direction == self.settings.Direction['Left']:
            nextCenterX = self.rect.centerx - self.settings.speed
            nextCenterY = self.rect.centery
        elif self.direction == self.settings.Direction['Up']:
            nextCenterX = self.rect.centerx
            nextCenterY = self.rect.centery - self.settings.speed
        elif self.direction == self.settings.Direction['Right']:
            nextCenterX = self.rect.centerx + self.settings.speed
            nextCenterY = self.rect.centery
        elif self.direction == self.settings.Direction['Down']:
            nextCenterX = self.rect.centerx
            nextCenterY = self.rect.centery + self.settings.speed
        
        for i in self.imageList:
            [image, rect] = i

            tempX = rect.centerx
            tempY = rect.centery
            rect.centerx = nextCenterX
            rect.centery = nextCenterY
            nextCenterX = tempX
            nextCenterY = tempY

            
    def addTail(self, foodGroup):
        food = foodGroup.sprites().pop()

        spritesPath = path.dirname(__file__) + '/sprites/body.bmp'
        image = pygame.image.load(spritesPath)
        self.imageList.append([image, food.rect])