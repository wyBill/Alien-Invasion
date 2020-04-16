# Authoer: wuyin
# Time: 2020/4/4

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import pygame
import game_functions as gf


def run_game():
    # initial the pygame and create a object
    pygame.init()

    # initial the settings
    alien_settings = Settings()

    # set the screen
    screen = pygame.display.set_mode((alien_settings.screen_width, alien_settings.screen_height))

    # create a ship
    ship = Ship(screen, alien_settings)

    # set the caption of the game
    pygame.display.set_caption('Alien Invasion')

    # create the bullets group
    bullets = Group()

    # create the aliens group
    alien = Alien(alien_settings, screen)
    aliens = Group()

    # running the game
    while True:
        # running the game
        gf.check_events(alien_settings, screen, ship, bullets)
        ship.update()

        # remove the used bullets
        gf.update_bullets(bullets)

        # refresh the screen
        gf.update_screen(alien_settings, screen, ship, bullets, alien)


if __name__ == '__main__':
    run_game()