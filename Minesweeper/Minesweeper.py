import random
from datetime import datetime

import pygame

from Board import Board
from Game_Logic import GameLogic
from Tile import Tile


class Minesweeper:
    board: Board
    logic: GameLogic
    tiles: list[Tile]

    def __init__(self, width, height):
        super().__init__()
        random.seed(datetime.now().timestamp())
        self.last_reset = datetime.now()

        self.width = width
        self.height = height
        self.tiles = []

        tile_size = 40

        self.board = Board(self.width, self.height, tile_size)
        self.setup_board()

        self.logic = GameLogic(self.tiles, self.width, self.height, tile_size)
        self.logic.setup()

    def setup_board(self):
        self.tiles = []

        for y in range(self.height):
            for x in range(self.width):
                self.tiles.append(Tile(self.board, x, y))

    def update(self):
        self.logic.update()
        self.board.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.logic.won and not self.logic.lost:
                self.update()

            if pygame.key.get_pressed()[pygame.K_RETURN] and (datetime.now() - self.last_reset).total_seconds() > 1:
                print("Game reset")
                self.__init__(self.width, self.height)

        pygame.quit()

    def start(self):
        self.run()
