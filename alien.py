# Author: wuyin
# Time: 2020/4/4

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, alien_settings, screen):
        # initialize
        super().__init__()
        self.screen = screen
        self.alien_settings = alien_settings

        # load the image of alien
        self.image = pygame.image.load('sources/alien.bmp')
        self.rect = self.image.get_rect()

        # set the position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save the position
        self.x = float(self.rect.x)

    def blitme(self):
        # image and rect
        self.screen.blit(self.image, self.rect)