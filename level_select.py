import pygame
import sys
import os

class LevelSelect():
    def __init__(self):
        pygame.init()
        self.width, self.height = 1280, 1024
        self.display = pygame.Surface((self.width, self.height))
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('necropolis')


    def terminate(self):
        pygame.quit()
        sys.exit()

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', 'select_level1.jpg')
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

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
            self.background = pygame.image.load('data/select_level1.jpg')
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()


if __name__ == '__main__':
    app = LevelSelect()
    app.run_game()



