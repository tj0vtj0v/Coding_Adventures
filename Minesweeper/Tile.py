from Board import Board


class Tile:
    board: Board
    size: int
    x: int
    y: int

    surrounding_bombs: int = 0
    bomb: bool = False
    revealed: bool = False
    flagged: bool = False

    def __init__(self, board: Board, x: int, y: int):
        self.board = board
        self.x = x
        self.y = y

    def draw(self):
        if self.flagged:
            self.board.draw_tile(self.x, self.y, (150, 250, 150), "F")
        elif not self.revealed:
            self.board.draw_tile(self.x, self.y, (100, 100, 100), " ")
        elif self.bomb:
            self.board.draw_tile(self.x, self.y, (250, 150, 150), "X")
        else:
            self.board.draw_revealed_tile(self.x, self.y, self.surrounding_bombs)

    def reveal(self):
        self.flagged = False
        self.revealed = True

    def flag(self):
        self.flagged = not self.flagged

    def plant_bomb(self):
        self.bomb = True
