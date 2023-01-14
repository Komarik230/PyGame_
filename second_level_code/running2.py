import pygame, sys
from map import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
level = Level(map2, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    background = pygame.image.load("level2.jpg")
    screen.blit(background, (0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)
