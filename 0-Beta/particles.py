from random import randint
from config import *

# ------------ Particles ------------
class Particle:
    def __init__(self):
        self.color = DEFAULT_PART_COLOR
        self.symbol = "V"
        self.priority = 0
        return

    def __repr__(self):
        return f'{self.__class__.__name__}({self.color})'

    def __str__(self):
        return f'{PARTICLE_SYMBOLS[self.__class__.__name__]}'
    
    def tick(self, neighbors):
        for moves in PARTICLE_MOVE_PATTERNS[self.symbol]:
            indexing = (-1, 1)[randint(0, 1)]
            for move in moves[::indexing]:
                if neighbors[move[0]][move[1]].symbol == 'V':
                #if neighbors[move[0]][move[1]].priority < self.priority:
                    return (move[0] - 1, move[1] - 1), None
        return False, None


class Edge(Particle):
    def __init__(self):
        super().__init__()
        self.symbol = "E"
        self.priority = 999999
        return

# Move Priority
# X X X
# X O X
# X X X
# All possible moves, assuming for now that particles can only move one space.
# Rank Choices with:
# 0 Default ie no movement
# 1 First Choice
# 2 Second Choice
# ...
# 
# Choices are based in order 
class Water(Particle):
    def __init__(self):
        super().__init__()
        self.color = BLUE
        self.symbol = "W"
        self.priority = 1
        return


class Sand(Particle):
    def __init__(self):
        super().__init__()
        self.symbol = "S"
        self.color = SAND_COLOR
        self.priority = 2
        return


# --------------- Box ---------------
class Box:
    def __init__(self):
        self.particles = []
        self.fill_particles()
        return
    
    def fill_particles(self):
        self.particles = []
        for r in range(GRID_SIZE[0]):
            self.particles.append([])
            for c in range(GRID_SIZE[1]):
                self.particles[r].append(Particle())
        return

    def __getitem__(self, i):
        return self.particles[i]

    def display(self):
        for r in self.particles:
            for c, p in enumerate(r):
                print(str(p), end=[" ","\n"][c == len(r)-1])
        print()
        return
    
    def replace(self, r: int, c: int, p: Particle):
        self.particles[r][c] = p
        return

    def get_3x3_slice_with_edges(self, r, c, fill_value=Edge()):
        rows, cols = len(self.particles), len(self.particles[0])
        neighbors = []

        for i in range(r - 1, r + 2):
            row = []
            for j in range(c - 1, c + 2):
                if 0 <= i < rows and 0 <= j < cols:
                    row.append(self.particles[i][j])
                else:
                    row.append(fill_value)
            neighbors.append(row)

        return neighbors

    def tick(self):
        new_box = [[Particle() for c in range(GRID_SIZE[1])] for r in range(GRID_SIZE[0])]

        for r in range(GRID_SIZE[0]):
            for c in range(GRID_SIZE[1]):
                if self.particles[r][c].symbol != "V":
                    neighbors = self.get_3x3_slice_with_edges(r, c)
                    self.particles[max(r-1, 0):min(r+1, GRID_SIZE[1]-1)][max(c-1, 0):min(c+1, GRID_SIZE[0]-1)]
                    movement, new_p = self.particles[r][c].tick(neighbors)
                    if movement:
                        if new_p is None:
                            new_p = self.particles[r][c]

                        new_x = r + movement[0]
                        new_y = c + movement[1]
                        if new_box[new_x][new_y].symbol == "V":
                            # Just Move
                            new_box[new_x][new_y] = new_p
                        else:
                            # Switch
                            new_box[r][c] = new_p
                    else:
                        new_box[r][c] = self.particles[r][c]

        self.particles = new_box
        return
