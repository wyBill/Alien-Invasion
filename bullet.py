# Author: wuyin
# Time: 2020/4/4

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, alien_settings, screen, ship):
        # initialize
        super().__init__()
        self.screen = screen
        self.alien_settings = alien_settings
        self.ship = ship

        # create a bullte
        self.rect = pygame.Rect(0, 0, alien_settings.bullet_width, alien_settings.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        # save the y position in float
        self.y = float(self.rect.y)

        # color
        self.color = self.alien_settings.bullet_color

        # speed
        self.speed = self.alien_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)