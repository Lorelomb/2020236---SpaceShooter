import pygame
from ship import Ship
import constants as c
from background import BG
from enemy_spawner import EnemySpawner

# Game Setup
display = pygame.display.set_mode(c.DISPLAY_SIZE)
fps = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

# Object setup
bg = BG()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
player = Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = EnemySpawner()


running = True
while running:
    # Tick Clock
    clock.tick(fps)

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.vel_x = -player.speed
            elif event.key == pygame.K_d:
                player.vel_x = player.speed
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.vel_x = 0
            elif event.key == pygame.K_d:
                player.vel_x = 0

    # Update all the objects
    bg_group.update()
    sprite_group.update()
    enemy_spawner.update()

    # Check collision
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()

    # Render the display
    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    pygame.display.update()
