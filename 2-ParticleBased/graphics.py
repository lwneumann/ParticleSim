import pygame
from config import *
from box import *


class Window:
    def __init__(self):
        self.setup()
        self.run()
        return

    def setup(self):
        # Setup
        pygame.init()
        pygame.font.init()

        # Make things
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
        pygame.display.set_caption(SCREEN_TITLE)
        
        # Get internals
        self.box = Box()
        self.saves = [Box() for b in range(SAVE_SLOTS)]
        self.tick_parity = 0
        return

    def draw_square(self, color, x, y, w=0, size=SQUARE_SIZE):
        pygame.draw.rect(self.screen, color, (x, y, size, size), width=w)
        return

    def draw_grid(self):
        # Draw Grid
        for r in range(GRID_SIZE[0]):
            for c in range(GRID_SIZE[1]):
                x = EDGE_BUFFER + (BUFFER_SIZE * (c+1)) + (c * SQUARE_SIZE)
                y = EDGE_BUFFER + (BUFFER_SIZE * (r+1)) + (r * SQUARE_SIZE)
                self.draw_square(self.box[r][c].color, x, y)

        # Draw Selection
        x = (self.box.cursor[1] * SQUARE_SIZE) + ((self.box.cursor[1]+1) * BUFFER_SIZE) + EDGE_BUFFER
        y = (self.box.cursor[0] * SQUARE_SIZE) + ((self.box.cursor[0]+1) * BUFFER_SIZE) + EDGE_BUFFER
        box_size = self.box.cursor_size * SQUARE_SIZE + (self.box.cursor_size - 1) * BUFFER_SIZE
        self.draw_square(SELECTED_COLOR, x, y, w=SELECTED_WIDTH, size=box_size)
        return

    def draw_menu(self):
        # Draw Selected
        self.draw_square(self.box.selected_particle.color,
                         MENU_X_START, EDGE_BUFFER,
                         size=SELECTED_PREVIEW_SIZE)
        return

    def draw_screen(self):
        # Base
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw
        self.draw_grid()
        self.draw_menu()

        # Update
        pygame.display.flip()
        return

    def load(self, slot):
        self.box = self.saves[slot]
        return

    def save(self, slot):
        self.saves[slot] = self.box
        return

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            # --- Events and other keystrokes
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_PLUS:
                        self.box.scroll(1)
                    elif event.key == pygame.K_KP_MINUS:
                        self.box.scroll(-1)

            # Key Presses
            keys = pygame.key.get_pressed()
            # Quit
            if keys[pygame.K_ESCAPE]:
                running = False
            # Reset
            if keys[pygame.K_r]:
                self.box = Box()
            # Scroll
            if keys[pygame.K_EQUALS]:
                self.box.scroll(1)
            elif keys[pygame.K_MINUS]:
                self.box.scroll(-1)
            # Print Box
            if keys[pygame.K_p]:
                self.box.display()
            # Move Selected
            if keys[pygame.K_LEFT]:
                self.box.select([0, -1])
            elif keys[pygame.K_RIGHT]:
                self.box.select([0, 1])
            if keys[pygame.K_UP]:
                self.box.select([-1, 0])
            elif keys[pygame.K_DOWN]:
                self.box.select([1, 0])
            # Change Particles
            if keys[pygame.K_s]:
                self.box.selected_particle = Sand()
            elif keys[pygame.K_w]:
                self.box.selected_particle = Water()
            elif keys[pygame.K_a]:
                self.box.selected_particle = Stone()
            elif keys[pygame.K_e]:
                self.box.selected_particle = Empty()
            elif keys[pygame.K_v]:
                self.box.selected_particle = Void()
            elif keys[pygame.K_g]:
                self.box.selected_particle = Generator()
            elif keys[pygame.K_t]:
                self.box.selected_particle = Tree(1)
            # Save Slots
            if keys[pygame.K_LSHIFT]:
                if keys[pygame.K_KP1]:
                    self.save(1)
            # Load slots
            else:
                if keys[pygame.K_KP1]:
                    self.load(1)
            # Add Particle
            if keys[pygame.K_SPACE]:
                self.box.write(self.tick_parity)

            # Update
            self.draw_screen()
            self.box.tick(self.tick_parity)
            self.tick_parity += 1
            # Maintain FPS
            clock.tick(FPS)
            if clock.get_fps() < FPS - 1:
                print(f"Running Slower than {FPS}: {clock.get_fps()}")

        # Close
        pygame.font.quit()
        pygame.quit()
        return


if __name__ == "__main__":
    w = Window()

