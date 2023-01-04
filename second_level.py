import pygame
from block import Block
from map import block_size
from player import Player

class LevelSecond:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0

    def setup_level(self, layout):
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x, y = col_index * block_size, row_index * block_size
                if cell == 'X':
                    block = Block((x, y), block_size)
                    self.blocks.add(block)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)


    def run(self):
        self.blocks.update(self.world_shift)
        self.blocks.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.player.update()
