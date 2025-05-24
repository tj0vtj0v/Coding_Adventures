import random

import pygame

from Tile import Tile


class GameLogic:
    def __init__(self, tiles, width, height, tile_size):
        self.tiles: list[Tile] = tiles
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.bombs = []

        self.won = False
        self.lost = False

        self.last_pressed = [False, False, False]

    def setup(self):
        self.place_bombs()
        self.inform_tiles()

    def place_bombs(self):
        self.bombs = []

        while len(self.bombs) < (self.width * self.height) // 10:
            number = random.randint(0, self.width * self.height - 1)
            if number not in self.bombs:
                self.bombs.append(number)

    def inform_tiles(self):
        for bomb in self.bombs:
            tile = self.tiles[bomb]
            tile.plant_bomb()

            for i in range(-1, 2):
                for j in range(-1, 2):
                    index = bomb + i + j * self.width

                    if 0 <= index < len(self.tiles):
                        is_no_bomb = not self.tiles[index].bomb
                        is_not_wrapped = abs((bomb % self.width) - (index % self.width)) <= 1
                        if is_no_bomb and is_not_wrapped:
                            self.tiles[index].surrounding_bombs += 1

    def recursive_reveal(self, tile_id: int):
        self.tiles[tile_id].reveal()

        if self.tiles[tile_id].surrounding_bombs == 0 and not self.tiles[tile_id].bomb:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue

                    index = tile_id + i + j * self.width
                    if 0 <= index < len(self.tiles):
                        is_no_bomb = not self.tiles[index].bomb
                        is_not_wrapped = abs((tile_id % self.width) - (index % self.width)) <= 1
                        already_manipulated = self.tiles[index].revealed or self.tiles[index].flagged

                        if is_no_bomb and is_not_wrapped and not already_manipulated:
                            self.recursive_reveal(index)

    def check_for_game_over(self):
        game_is_won = True
        for tile in self.tiles:
            if not tile.bomb and not tile.revealed:
                game_is_won = False

            tile.draw()

        if game_is_won and not self.lost:
            self.won = True
            print("Congratulations! You've cleared the board without hitting a bomb.")

        elif self.lost:
            print("Game Over! You hit a bomb.")
            for tile in self.tiles:
                if tile.bomb:
                    tile.reveal()
                    tile.draw()

    def process_pressed_mouse_button(self, tile_id: int, pressed: tuple[bool, bool, bool]):
        tile = self.tiles[tile_id]

        if pressed[0] and pressed[0] ^ self.last_pressed[0]:  # left click
            if not tile.flagged:
                self.recursive_reveal(tile_id)

                if tile.bomb:
                    self.lost = True

        if pressed[1] and pressed[1] ^ self.last_pressed[1]:  # middle click
            pass

        if pressed[2] and pressed[2] ^ self.last_pressed[2]:  # right click
            if not tile.revealed:
                tile.flag()

    def update(self):
        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        tile_id = (x // self.tile_size) + (y // self.tile_size) * self.width

        if 0 <= tile_id < len(self.tiles):
            self.process_pressed_mouse_button(tile_id, pressed)

        self.last_pressed = pressed

        self.check_for_game_over()
