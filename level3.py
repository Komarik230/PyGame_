import pygame
import random


pygame.init()
Width = 1024
Height = 640
screen = pygame.display.set_mode((Width, Height))
fps = 60
clock = pygame.time.Clock()
pygame.display.set_caption('data/necropolis')
pygame.display.set_icon(pygame.image.load('data/scull.png'))
font_path = 'font.ttf'
font_large = pygame.font.Font(font_path, 48)
font_small = pygame.font.Font(font_path, 26)

game_over = False
retry_text = font_small.render('press to restart', True, (255, 255, 255))
retry_rect = retry_text.get_rect()
retry_rect.midtop = (Width // 2, Height // 2)

best_text = font_large.render('best result:', True, (255, 255, 255))
best_rect = best_text.get_rect()
best_rect.midtop = (200, 560)

ground_image = pygame.image.load('data/floor.png')
ground_image = pygame.transform.scale(ground_image, (1024, 80))
GROUND_H = ground_image.get_height()

player_image = pygame.image.load('data/skeleton.png.')
player_image = pygame.transform.scale(player_image, (100, 200))

bg_image = pygame.image.load('data/level3_bg.jpg')
gr_speed = 3

enemy_image = pygame.image.load('data/tomb.png')
enemy_image = pygame.transform.scale(enemy_image, (100, 100))

enemy_dead_image = pygame.image.load('data/dead_tomb.png')
enemy_dead_image = pygame.transform.scale(enemy_dead_image, (100, 100))

pygame.mixer.music.load('data/mus_level3.mp3')
pygame.mixer.music.play(-1)



class Sprites:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 3
        self.jump_speed = -12
        self.gravity = 0.5
        self.is_grounded = False  # находимся на земле или нет
        self.gr_x = 0
        self.is_out = False  # упал за карту или нет
        self.is_dead = False
        self.lenght = 5

    def handle_input(self): # ручной ввод/ввод пользователя
        pass

    def kill(self, dead_image):
        self.image = dead_image
        self.is_dead = True
        self.x_speed = -self.x_speed
        self.y_speed = self.jump_speed

    def update(self):
        self.rect.x += self.x_speed
        self.y_speed += self.gravity
        self.rect.y += self.y_speed

        if self.is_dead:
            if self.rect.top > Height - GROUND_H:
                self.is_out = True
        else:
            self.handle_input()

            if self.rect.bottom > Height - GROUND_H:
                self.is_grounded = True
                self.y_speed = 0
                self.rect.bottom = Height - GROUND_H

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(Sprites):
    def __init__(self):
        super().__init__(player_image)
        self.respawn()

    def handle_input(self):
        self.x_speed = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.rect.x <= Width // 2:
                self.gr_x += gr_speed
            if self.rect.x > 100:
                self.x_speed = -self.speed

        elif keys[pygame.K_d]:
            if self.rect.x >= Width // 2:
                self.gr_x -= gr_speed

            if self.rect.x < 800:
                self.x_speed = self.speed

        if self.gr_x == -1024:
            self.gr_x = 0

        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.is_grounded:
            self.is_grounded = False
            self.jump()

    def jump(self):
        self.y_speed = self.jump_speed

    def respawn(self):
        self.is_out = False
        self.is_dead = False
        self.rect.midbottom = (Width // 2, Height - GROUND_H)

    def draw_main(self):
        screen.blit(bg_image, (0, 0))
        screen.blit(ground_image, (self.gr_x, 640 - GROUND_H))
        screen.blit(ground_image, (self.gr_x - 1024, 640 - GROUND_H))
        for i in range(1, self.lenght + 1):
            screen.blit(ground_image, (self.gr_x + i * 1024, Height - GROUND_H))


class Tomb(Sprites):
    def __init__(self):
        super().__init__(enemy_image)
        self.spawn()

    def spawn(self):
        direction = random.randint(0, 1)
        if direction == 0:
            self.x_speed = self.speed
            self.rect.bottomright = (0, 0)
        else:
            self.x_speed = -self.speed
            self.rect.bottomleft = (Width, 0)

    def update(self):
        super().update()
        if self.x_speed > 0 and self.rect.left > Width or self.x_speed < 0 and self.rect.right < 0:
            self.is_out = True


def main():
    player = Player()
    score = 0
    enemies = []
    delay = 2000 # задержка спавна мобов
    spawn_delay = delay # как часто спавнятся мобы(интервал)
    increase = 1.01
    last_spawn_time = pygame.time.get_ticks()
    running = True
    while running:
        with open("best_res.txt", 'rb') as f:
            best_result = int(f.read())

        player.draw_main()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.mixer.music.stop()
            elif e.type == pygame.KEYDOWN:
                if player.is_out:
                    score = 0
                    spawn_delay = delay
                    last_spawn_time = pygame.time.get_ticks()
                    player.respawn()
                    enemies.clear()
        clock.tick(fps)
        score_text = font_large.render(str(score), True, (255, 255, 255))
        score_rect = score_text.get_rect()

        best_res_text = font_large.render(str(best_result), True, (255, 255, 255))
        best_res_rect = best_res_text.get_rect()
        best_res_rect.midtop = (410, 560)

        if player.is_out: # герой умер
            score_rect.midbottom = (Width // 2, Height // 2)
            screen.blit(retry_text, retry_rect)
            screen.blit(best_text, best_rect)
            if score > best_result:
                best_result = score
                with open("best_res.txt", 'w') as f:
                    f.write(str(best_result))
            screen.blit(best_res_text, best_res_rect)
        else: # герой все еще жив
            player.update()
            player.draw(screen)

            now = pygame.time.get_ticks()
            time_passed = now - last_spawn_time
            if time_passed > spawn_delay:
                last_spawn_time = now
                enemies.append(Tomb())
            for enemy in list(enemies):
                if enemy.is_out:
                    enemies.remove(enemy)
                else:
                    enemy.update()
                    enemy.draw(screen)

                if not player.is_dead and not enemy.is_dead and player.rect.colliderect(enemy.rect):
                    if player.rect.bottom - player.y_speed < enemy.rect.top:
                        enemy.kill(enemy_dead_image)
                        player.jump()
                        score += 1
                        spawn_delay = delay / (increase ** score)

                    else:
                        player.kill(player_image)
            score_rect.midtop = (Width // 2, 5)
        screen.blit(score_text, score_rect)
        pygame.display.flip()


main()
quit()
