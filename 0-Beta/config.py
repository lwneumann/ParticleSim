# Colors
BLACK = 0, 0, 0
GRAY = 60, 60, 60
BLUE = 3, 165, 252
WHITE = 255, 255, 255

# Color Choices
BACKGROUND_COLOR = GRAY
DEFAULT_PART_COLOR = BLACK
SELECTED_COLOR = WHITE
SAND_COLOR = 246,215,176

# Grid
GRID_SIZE = [20, 20]
SQUARE_SIZE = 15
BUFFER_SIZE = 0
SCREEN_SIZE = [
    GRID_SIZE[1] * SQUARE_SIZE +
    (GRID_SIZE[1]+1) * BUFFER_SIZE,
    GRID_SIZE[0] * SQUARE_SIZE +
    (GRID_SIZE[0]+1) * BUFFER_SIZE
]

# Game Settings
FPS = 10

PARTICLE_SYMBOLS = {
    "Particle": "V",
    "Water": "W",
    "Sand": "S"
}
SYMBOL_TO_PART = {
    s: p for p, s in PARTICLE_SYMBOLS.items()
}

PARTICLE_MOVE_PATTERNS = {
    # y, x
    "W": [[[2, 1]],
          [[2, 0], [2, 2]],
          [[1, 0], [1, 2]]],
    "S": [[[2, 1]],
          [[2, 0], [2,2]]]
}

SELECTED_WIDTH = 2

# Extra
SCREEN_TITLE = "Wee wa"
