import random
import sys
import pygame

pygame.init()
size = width, height = [1024, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

particles = []
text_surf = pygame.image.load("data\\game over.png")
text_rect = text_surf.get_rect(center=(width // 2, height // 2))

#  заставка
def update():
    particle = {
        "pos": [
            random.randint(0, width),
            random.randint(0, 0)],
        "velocity": [0, random.uniform(0, 3)]
    }

    particles.append(particle)

    for p in particles:
        p['pos'][0] += p['velocity'][0]
        p['pos'][1] += p['velocity'][1]


def render():
    for p in particles:
        pygame.draw.circle(screen, (148, 16, 16), p['pos'], 10)
    screen.blit(text_surf, text_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit()
    update()
    render()

    pygame.display.update()
    clock.tick(60)
