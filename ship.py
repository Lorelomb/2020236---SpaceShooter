import pygame
import constants as c
from bullet import Bullet


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('Assets/spaceship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height * 2
        self.bullets = pygame.sprite.Group()
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5

    def update(self):
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        self.rect.y += self.vel_y


    def shoot(self):
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2) -4
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)
