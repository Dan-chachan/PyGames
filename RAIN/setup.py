import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (74, 255, 54)
RED = (255, 33, 31)
BLUE = (59, 71, 255)
AQUA = (49, 225, 232)
PINK = (232, 42, 204)
ORANGE = (255, 85, 14)
YELLOW = (232, 194, 55)
DEEP_PURPLE = (35, 24, 46)

PI = 3.141592653

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(screen_size)

GRID_SIZE = 50

SQUARES_WID = WINDOW_WIDTH / GRID_SIZE
SQUARES_HEI = WINDOW_HEIGHT / GRID_SIZE


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()