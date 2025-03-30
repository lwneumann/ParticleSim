from random import randint
from config import *


class Box:
    def __init__(self):
        self.particles = [
            ["E" for c in range(GRID_SIZE[1])]
            for r in range(GRID_SIZE[0])
        ]
        return

    def __getitem__(self, i):
        return self.particles[i]

    def __repr__(self):
        return f"Box({self.particles})"

    def display(self):
        for r in self.particles:
            print(r)
        print()
        return

    def replace(self, r, c, p):
        self[r][c] = p
        return

    def move_p(self, r, c, n_r, n_c, p):
        # r, c     - row, col
        # n_r, n_c - new row, new col
        # p        - The particle moving from r,c -> n_r,n_c

        # Void eats anything
        if self[n_r][n_c] == "V":
            self[r][c] = "E"
        # Others actually move
        else:
            self[r][c], self[n_r][n_c] = self[n_r][n_c], p
        return

    def move_particle(self, r, c):
        for moves in PARTICLE_MOVE_PATTERNS[self[r][c]]:
            indexing = (-1, 1)[randint(0, 1)]
            # Randomize movement choice. For now only really works with two options thou
            # So ideally add something to randomize three choices if that is implemented
            for move in moves[::indexing]:
                if SCREEN_WRAP <= r + move[0] < GRID_SIZE[0] and SCREEN_WRAP <= c + move[1] < GRID_SIZE[1]:
                    empty_space = self[r + move[0]][c + move[1]] in MOVEABLE_SPACES
                    swap = self[r + move[0]][c + move[1]] == "W" and self[r][c] == "S"
                    if empty_space or swap:
                        self.move_p(r, c, r + move[0], c + move[1], self[r][c])
        return

    def tick(self):
        # For all particles
        for r in list(range(GRID_SIZE[0]))[::-1]:
            for c in range(GRID_SIZE[1]):
                # Behave in a way
                if self[r][c] not in NONMOVING_OBJECTS:
                    self.move_particle(r, c)
        return
