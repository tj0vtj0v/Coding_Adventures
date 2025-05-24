import pygame


class Board:
    clock = None
    screen = None

    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size

        self.create_screen()

    def create_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width * self.tile_size, self.height * self.tile_size))
        self.clock = pygame.time.Clock()

    def draw_revealed_tile(self, x, y, surrounding_bombs):
        if surrounding_bombs > 0:
            self.draw_tile(x, y, (150, 150, 150), str(surrounding_bombs))
        else:
            self.draw_tile(x, y, (150, 150, 150), " ")

    def draw_tile(self, x, y, color, letter):
        fill = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
        pygame.draw.rect(self.screen, color, fill)

        self.draw_border(x, y)
        self.draw_letter(x, y, letter)

    def draw_letter(self, x, y, letter):
        font = pygame.font.Font(None, 36)
        text = font.render(letter, True, (0, 0, 0))
        text_rect = text.get_rect(
            center=(x * self.tile_size + self.tile_size // 2, y * self.tile_size + self.tile_size // 2))
        self.screen.blit(text, text_rect)

    def draw_border(self, x, y):
        border = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
        pygame.draw.rect(self.screen, (200, 200, 200), border, 1)

    def update(self):
        pygame.display.flip()
        self.clock.tick(30)
        self.screen.fill((0, 0, 0))
