import os
import sys
import pygame
from subprocess import call


class App:
    def __init__(self): # окно приложения
        pygame.init()
        self.width, self.height = 1024, 640
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('necropolis')
        pygame.display.set_icon(pygame.image.load('data/scull.png'))
        pygame.key.set_repeat(200, 70)
        self.fps = 50

    def terminate(self):
        pygame.quit()
        sys.exit()

    def load_image(self, name, colorkey=None):  # загрузка изображений
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

    def Coins(self):  # показ монет в главном меню
        font_path = 'font.ttf'
        font_small = pygame.font.Font(font_path, 26)
        with open('info.txt', 'rb') as f:
            coins = int(f.read())
        coins_text = font_small.render(str(coins), True, (255, 255, 255))
        coins_rect = coins_text.get_rect()
        coins_rect.midtop = (970, 15)
        self.screen.blit(coins_text, coins_rect)

    def start_screen(self):  # заставка
        fon = pygame.transform.scale(self.load_image('splash.jpg'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    app.select_level1()
                    return  # начинаем игру
            pygame.display.flip()
            self.clock.tick(self.fps)

    def select_level1(self):  # загрузка первого уровня в главном меню
        fon = pygame.transform.scale(self.load_image('select_level1.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        app.Coins()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        app.select_level2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    call(["python", "level1.py"])
            pygame.display.flip()

    def select_level2(self):  # загрузка второго уровня в главном меню
        fon = pygame.transform.scale(self.load_image('select_level2.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        app.Coins()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        app.select_level1()
                    if event.key == pygame.K_RIGHT:
                        app.select_level3()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    call(["python", "level2.py"])
            pygame.display.flip()

    def select_level3(self):  # загрузка третьего уровня в главном меню
        fon = pygame.transform.scale(self.load_image('select_level3.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        app.Coins()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        app.select_level2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    call(["python", "level3.py"])
            pygame.display.flip()

    def run_game(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                key = pygame.key.get_pressed()

            self.screen.fill(pygame.Color('black'))
            pygame.display.flip()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    app = App()
    app.start_screen()
    app.run_game()
