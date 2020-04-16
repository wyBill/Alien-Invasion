# Author: wuyin
# Time: 2020/4/4

import pygame


class Ship():
    def __init__(self, screen, alien_settings):
        # initialize
        self.screen = screen
        self.alien_settings = alien_settings

        # load the image and set the configuration
        self.image = pygame.image.load('sources/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set every ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # moving mark
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.alien_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.alien_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= self.alien_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.alien_settings.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)