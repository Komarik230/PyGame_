import pygame, sys, os
from map import *
from subprocess import call
from first_and_second_general import Coin, End, Player, ParticleEffect


def music_play(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Звуковой файл '{fullname}' не найден")
        sys.exit()
    pygame.mixer.music.load(fullname)
    pygame.mixer.music.play(-1)


def load_screen_im(name, colorkey=None):
    fullname = os.path.join(name)
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


class Tile(pygame.sprite.Sprite):
    # Класс плиток
    def __init__(self, pos, size):
        super().__init__()
        self.image = load_screen_im("data\\box.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Monstr(pygame.sprite.Sprite):
    # Класс Монстров
    def __init__(self, pos, size):
        super().__init__()
        self.image = load_screen_im("data\\monstr.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, x_shift):
        self.rect.x += x_shift


class Level:
    """Класс, отвечающий за настройку уровня
    create_jump_particles() создание пыли при прижках
    get_player_on_ground() выявление, где находится игрок
    create_landing_dust() создание пыли при беге
    setup_level() вывод уровня на экран при помощи чтения данных из файла map1
    scroll_x() перемещение карты в месте с героем
    horizontal_movement_collision() проверка на наличие столкновений по вертикали с плиткой
    vertical_movement_collision() проверка на наличие столкновений по горизонтали с плиткой
    collide_with_money_and_monstr() проверка на столкновение с монетами, сбор монет, проверка на столкновение с монстрами
    successful_end() появление заставки при успешном прохождении уровня
    run() запуск функций
    """
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False
        self.count = 0

    def create_jump_particles(self, pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)
        jump_particle_sprite = ParticleEffect(pos, 'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            if self.player.sprite.facing_right:
                offset = pygame.math.Vector2(10, 15)
            else:
                offset = pygame.math.Vector2(-10, 15)
            fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset, 'land')
            self.dust_sprite.add(fall_dust_particle)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.mogilas = pygame.sprite.Group()
        self.monstrs = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'C':
                    coin = Coin((x, y), tile_size)
                    self.coins.add(coin)
                if cell == 'E':
                    mogila = End((x, y), tile_size)
                    self.mogilas.add(mogila)
                if cell == 'M':
                    monstr = Monstr((x, y), tile_size)
                    self.monstrs.add(monstr)
                if cell == 'P':
                    player_sprite = Player((x, y), self.display_surface, self.create_jump_particles)
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < WIDTH / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > WIDTH - (WIDTH / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False

    def collide_with_money_and_monstr(self):
        player = self.player.sprite
        for coin in self.coins.sprites():
            if pygame.sprite.collide_rect(player, coin):
                self.count += 1  # монетки собираются
                coin.kill()
                with open('info.txt', 'w', encoding='utf-8') as f:
                    f.write(f'{self.count}')
        for monstr in self.monstrs.sprites():
            if pygame.sprite.collide_rect(player, monstr):
                call(["python", "game_over.py"])

    def successful_end(self):
        player = self.player.sprite
        if pygame.sprite.spritecollideany(player, self.mogilas):
            call(["python", "successful_end.py"])
            sys.exit()

    def run(self):
        self.dust_sprite.update(self.world_shift)
        self.dust_sprite.draw(self.display_surface)
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.mogilas.update(self.world_shift)
        self.mogilas.draw(self.display_surface)
        self.monstrs.update(self.world_shift)
        self.monstrs.draw(self.display_surface)
        self.scroll_x()
        self.player.update()
        self.horizontal_movement_collision()
        self.get_player_on_ground()
        self.vertical_movement_collision()
        self.create_landing_dust()
        self.player.draw(self.display_surface)
        self.collide_with_money_and_monstr()
        self.successful_end()




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
level = Level(map2, screen)
pygame.display.set_caption('necropolis')
pygame.display.set_icon(pygame.image.load('data\\scull.png'))
mus = music_play('data\\horror.mp3')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    background = pygame.image.load("data/level2.jpg")
    screen.blit(background, (0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)
