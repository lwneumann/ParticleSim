from config import *


class Empty:
    def __init__(self, sf=0):
        # Does it move
        self.moves = False
        # Can be entered
        self.ephemerate = True
        # Movement patterns
        self.movement_pattern = []
        # Color
        self.color = BLACK
        # Symbol
        self.symbol = "E"
        return
    
    def __eq__(self, value):
        return self.symbol == value

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol


class Sand(Empty):
    def __init__(self, sf=0):
        super().__init__()
        self.moves = True
        self.movement_pattern = [[[1, 0]],
                                 [[1, -1], [1, 1]]]
        self.ephemerate = False
        self.color = SAND_COLOR
        self.symbol = "S"
        return


class Water(Empty):
    def __init__(self, sf=0):
        super().__init__()
        self.moves = True
        self.ephemerate = False
        self.movement_pattern =  [[[1, 0]],
                                  [[1, -1], [1, 1]],
                                  [[0, -1], [0, 1]]]
        self.color = BLUE
        self.symbol = "W"
        return


class Stone(Empty):
    def __init__(self, sf=0):
        super().__init__()
        self.ephemerate = False
        self.color = STONE_COLOR
        self.symbol = "s"
        return


class Void(Empty):
    def __init__(self, sf=0):
        super().__init__()
        self.color = 115, 0, 161
        self.symbol = "V"
        return
    

class Generator(Empty):
    def __init__(self, sf=0):
        super().__init__()
        self.color = UNSET_GENERATOR
        self.spawn = None
        self.symbol = "G"
        self.movement_pattern = [
            [1, 0], [0, 1], [-1, 0], [0, -1]
        ]
        return
    
    def set(self, p):
        self.spawn = p
        self.ephemerate = False
        self.color = SET_GENERATOR
        self.moves = True
        return


class Tree(Empty):
    def __init__(self, sf=0):
        super().__init__()
        self.color = TREE_COLOR
        self.is_bark = True
        self.ephemerate = False
        self.moves = True
        self.symbol = "T"
        self.sf = sf
        return
    
    def leaf(self):
        self.color = LEAF_COLOR
        self.moves = False
        return

    def die(self):
        self.moves = False
        return
        