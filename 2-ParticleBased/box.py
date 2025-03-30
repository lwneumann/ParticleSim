from random import shuffle, random
from config import *
from particles import *


class Box:
    def __init__(self):
        self.particles = [
            [Empty() for c in range(GRID_SIZE[1])]
            for r in range(GRID_SIZE[0])
        ]
        self.cursor = [int(GRID_SIZE[0]/2), int(GRID_SIZE[1]/2)]
        self.cursor_size = CURSOR_SIZE
        self.selected_particle = Sand()
        return

    def select(self, new_pos, relative=True):
        if relative:    
            new_pos = [self.cursor[0] + new_pos[0],
                       self.cursor[1] + new_pos[1]]
        self.cursor = [max(0, min(new_pos[0], GRID_SIZE[0] - self.cursor_size)),
                       max(0, min(new_pos[1], GRID_SIZE[1] - self.cursor_size))]
        return

    def scroll(self, s):
        self.cursor_size = min(max(1, self.cursor_size + s), min(GRID_SIZE))

        if self.cursor_size % 2 == 1 and self.cursor_size > 1:
            self.select((-s, -s))
        else:
            self.select((0, 0))
        return

    def write(self, sf):
        if self.cursor_size == 1:
            self[self.cursor[0]][self.cursor[1]] = type(self.selected_particle)(sf)
        else:
            fill = [type(self.selected_particle)(sf) for i in range(self.cursor_size)]
            for r in range(self.cursor[0], self.cursor[0] + self.cursor_size):
                self[r][self.cursor[1]:self.cursor[1]+self.cursor_size] = fill
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

    def move_p(self, r, c, n_r, n_c, p):
        # r, c     - row, col
        # n_r, n_c - new row, new col
        # p        - The particle moving from r,c -> n_r,n_c

        # Void eats anything
        if self[n_r][n_c] == "V":
            self[r][c] = Empty()
        # Generator sets
        elif self[n_r][n_c] == "G" and self[n_r][n_c].spawn is None:
            self[n_r][n_c].set(self[r][c])
        # Others actually move
        else:
            self[r][c], self[n_r][n_c] = self[n_r][n_c], p
        return

    def in_bounds(self, pos):
        return 0 <= pos[0] < GRID_SIZE[0] and SCREEN_WRAP <= pos[1] < GRID_SIZE[1]

    def inindex(self, r, c):
        return self[r][c] if self.in_bounds((r, c)) else False

    def move_particle(self, r, c, tp):
        if self[r][c] == "G":
            for space in self[r][c].movement_pattern:
                new_pos = r + space[0], c + space[1]
                if self.in_bounds(new_pos):
                    if self[new_pos[0]][new_pos[1]] == "E":
                        self[new_pos[0]][new_pos[1]] = self[r][c].spawn
        elif self[r][c] == "T":
            # If death
            if random() <= TREE_DEATH_RATE:
                self[r][c].leaf()
            # If branch
            elif random() <= TREE_BRANCH_RATE:
                for bc in [c-1, c+1]:
                    if self.inindex(r, bc) == "E":
                        self[r][bc] = Tree(tp)
                self[r][c].die()
            # If Grow
            elif self.in_bounds([r-1, c]) and self[r-1][c] == "E":
                self[r-1][c] = Tree(tp)
                self[r][c].die()
        else:
            for moves in self[r][c].movement_pattern:
                # Randomize movement choice
                if len(moves) > 1:
                    shuffle(moves)
                for move in moves:
                    new_pos = r + move[0], c + move[1]
                    if 0 <= new_pos[0] < GRID_SIZE[0] and SCREEN_WRAP <= new_pos[1] < GRID_SIZE[1]:
                        # --- Move conditions
                        # Space that is enterable
                        empty_space = self[new_pos[0]][new_pos[1]].ephemerate
                        # Sand passes through water
                        swap = self[r][c] == "S" and self[new_pos[0]][new_pos[1]] == "W"
                        # --- Move
                        if empty_space or swap:
                            self.move_p(r, c, new_pos[0], c + move[1], self[r][c])
                            return
        return

    def tick(self, tp):
        # For all particles
        for r in list(range(GRID_SIZE[0]))[::-1]:
            col_indexing = r%2 * (-2) + 1
            for c in list(range(GRID_SIZE[1]))[::col_indexing]:
                # Behave in a way
                if self[r][c].moves:
                    if self[r][c] in UPWARD_P and self[r][c].sf != tp:
                        self.move_particle(r, c, tp)
                    else:
                        self.move_particle(r, c, tp)
        return
