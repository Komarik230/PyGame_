import os
import sys
import pygame


class LevelSelect():
    def __init__(self):
        pygame.init()
        self.width, self.height = 1024, 640
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('necropolis')
        pygame.display.set_icon(pygame.image.load('data/scull.png'))

    def terminate(self):
        pygame.quit()
        sys.exit()

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def select_level1(self):
        fon = pygame.transform.scale(self.load_image('select_level1.jpg'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        app.select_level2()
            pygame.display.flip()

    def select_level2(self):
        fon = pygame.transform.scale(self.load_image('select_level2.jpg'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        app.select_level1()
                    if event.key == pygame.K_RIGHT:
                        app.select_level3()
            pygame.display.flip()

    def select_level3(self):
        fon = pygame.transform.scale(self.load_image('select_level3.jpg'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        app.select_level2()
            pygame.display.flip()

    def run_game(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()

            self.screen.fill(pygame.Color('black'))
            pygame.display.flip()


if __name__ == '__main__':
    app = LevelSelect()
    app.select_level1()
    app.run_game()
