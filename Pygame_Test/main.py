import pygame

# Pygame initialization
pygame.init()

# init screen
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# game logic
points = []


def add_point(x, y):
    points.append({"pos": (x, y), "col": (255, 255, 255)})


def update_points():
    for point in points:
        new_col = point["col"][0] - 5
        if new_col < 0:
            points.pop(0)
        point["col"] = (new_col, new_col, new_col)


def draw_points():
    for point in points:
        pygame.draw.circle(screen, point["col"], point["pos"], radius=point["col"][0]//10)


# init in-game-clock
clock = pygame.time.Clock()

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # reset screen
    screen.fill((0, 0, 0))

    # init objects on screen
    x, y = pygame.mouse.get_pos()
    add_point(x, y)
    update_points()
    draw_points()

    #  print on screen
    pygame.display.flip()
    clock.tick(120)  # fps UND tick speed
