# Author: wuyin
# Time: 2020/4/4

from bullet import Bullet
import pygame
import sys


def check_events(alien_settings, screen, ship, bullets):
    # supervisor the key and the mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, alien_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, alien_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullets(bullets, alien_settings, screen, ship)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(alien_settings, screen, ship, bullets, alien):
    # set the background color
    screen.fill(alien_settings.bg_color)

    # show the ship
    ship.blitme()

    # show the alien
    alien.blitme()

    # draw all bullets
    for bullet in bullets:
        bullet.draw_bullet()

    # draw all aliens

    # refresh the screen
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.top < 0:
            bullets.remove(bullet)
        print(len(bullets))


def fire_bullets(bullets, alien_settings, screen, ship):
    if len(bullets) < alien_settings.bullets_allowed:
        new_bullet = Bullet(alien_settings, screen, ship)
        bullets.add(new_bullet)
