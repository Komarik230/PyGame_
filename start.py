import pygame, sys
from map import *
from second_level import LevelSecond


pygame.init()
WIDTH = 1024
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
level = LevelSecond(map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
