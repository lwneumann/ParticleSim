# ---- Game Settings
FPS = 20
# Vert, Horz
GRID_SIZE = [40, 40]
STARTING_POS = [4, 4]
SAVE_SLOTS = 9

# 0 = No Wrap
# 0 > Screen Wrap
SCREEN_WRAP = 0

# Objects that don't move
NONMOVING_OBJECTS = ["E", "V", "s"]
# Objects that an object can enter
MOVEABLE_SPACES = ["E", "V"]

PARTICLE_MOVE_PATTERNS = {
    # y, x
    "W": [[[1, 0]],
          [[1, -1], [1, 1]],
          [[0, -1], [0, 1]]],
    "S": [[[1, 0]],
          [[1, -1], [1, 1]]],
}

# E - Empty
#   -- Empty
# V - Void
#   -- Eats stuff
# W - Water
#   -- Flows down
# S - Sand
#   -- Falls down, through water
# s - Stone
#   -- Solid, doesn't move

# Graphics
SCREEN_TITLE = ":)"
SQUARE_SIZE = 10
BUFFER_SIZE = 0
EDGE_BUFFER = 10
MENU_WIDTH = SQUARE_SIZE*3
SELECTED_PREVIEW_SIZE = MENU_WIDTH
FONT_NAME = "broadway"
FONT_SIZE = 10
SELECTED_WIDTH = 2
# ----

# Dependant settings
SCREEN_SIZE = [
    GRID_SIZE[1] * SQUARE_SIZE +
    (GRID_SIZE[1]+1) * BUFFER_SIZE +
    EDGE_BUFFER * 3 + MENU_WIDTH,
    GRID_SIZE[0] * SQUARE_SIZE +
    (GRID_SIZE[0]+1) * BUFFER_SIZE +
    EDGE_BUFFER * 2
]
MENU_X_START = SCREEN_SIZE[0] - MENU_WIDTH - EDGE_BUFFER

# ---- Colors
BLACK = 0, 0, 0
GRAY = 60, 60, 60
BLUE = 3, 165, 252
WHITE = 255, 255, 255

# Color Choices
PARTICLE_COLORS = {
    "E": BLACK,
    "S": (246, 215, 176),
    "W": BLUE,
    "s": (140, 140, 140),
    "V": (115, 0, 161)
}
BACKGROUND_COLOR = GRAY
SELECTED_COLOR = WHITE

"""
To be added?

Moss
- Grows on stone
Tree
- Eats water to grow
Fire
- fire.

"""