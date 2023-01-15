import pygame, sys, os
from map import *
from level import Level


def music_play(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Звуковой файл '{fullname}' не найден")
        sys.exit()
    pygame.mixer.music.load(fullname)
    pygame.mixer.music.play(-1)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
level = Level(map2, screen)
pygame.display.set_caption('necropolis')
pygame.display.set_icon(pygame.image.load('scull.png'))
mus = music_play('horror.mp3')

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
