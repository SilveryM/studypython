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

            pass

            
    def addTail(self, foodGroup):
        food = foodGroup.sprites().pop()

        spritesPath = path.dirname(__file__) + '/sprites/body.bmp'
        image = pygame.image.load(spritesPath)
        rect = food.rect

        #只有头
        if len(self.imageList) == 1:
            headRect = self.imageList[0][1]
            if self.direction == self.settings.Direction['Left']:
                rect.centerx = headRect.centerx + self.settings.spriteSize
                rect.centery = headRect.centery
            elif self.direction == self.settings.Direction['Up']:
                rect.centerx = headRect.centerx
                rect.centery = headRect.centery + self.settings.spriteSize
            elif self.direction == self.settings.Direction['Right']:
                rect.centerx = headRect.centerx - self.settings.spriteSize
                rect.centery = headRect.centery
            elif self.direction == self.settings.Direction['Down']:
                rect.centerx = headRect.centerx
                rect.centery = headRect.centery - self.settings.spriteSize

        self.imageList.append([image, rect])

    def Reset(self):
        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery
        self.direction = self.settings.Direction['Left']

        image = self.imageList[0][0]
        self.imageList.clear()
        self.imageList.append([image, self.rect])