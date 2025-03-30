# ---- Game Settings
FPS = 10
# Vert, Horz
GRID_SIZE = [40, 40]
CURSOR_SIZE = 1
SAVE_SLOTS = 9

# Particle Settings
TREE_DEATH_RATE = 0.2
TREE_BRANCH_RATE = 0.15

# Particles that move up
UPWARD_P = ["T"]

# 0  - No Wrap
# -1 - Screen Wrap
SCREEN_WRAP = 0

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
# G - Generator
#   -- Generates first p that touches it
# T - Tree
#   -- Grows

# ---- Graphics
SCREEN_TITLE = ":)"
SQUARE_SIZE = 10
BUFFER_SIZE = 0
EDGE_BUFFER = 10
MENU_WIDTH = SQUARE_SIZE*3
SELECTED_PREVIEW_SIZE = MENU_WIDTH
FONT_NAME = "broadway"
FONT_SIZE = 10
SELECTED_WIDTH = 2

# ---- Dependant settings
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
BACKGROUND_COLOR = GRAY
SELECTED_COLOR = WHITE

UNSET_GENERATOR = 26, 189, 35
SET_GENERATOR = 59, 130, 62

SAND_COLOR = 246, 215, 176
STONE_COLOR = 140, 140, 140
TREE_COLOR = 105,75,55
LEAF_COLOR = 95,99,68

"""
To be added?

Moss
- Grows on stone
Tree
- Eats water to grow
Fire
- fire.

"""