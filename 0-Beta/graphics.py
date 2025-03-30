import pygame
from config import *
from particles import *


class Window:
    def __init__(self):
        self.setup()
        self.run()
        return

    def setup(self):
        # Setup Window
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
        pygame.display.set_caption(SCREEN_TITLE)
        
        # Get internals
        self.selected = [4, 4]
        self.selected_particle = Water()
        self.box = Box()
        return
    
    def inject(self):
        self.box.replace(self.selected[0], self.selected[1], self.selected_particle)
        return

    def draw_grid(self):
        for r in range(GRID_SIZE[0]):
            for c in range(GRID_SIZE[1]):
                x = (BUFFER_SIZE * (c+1)) + (c * SQUARE_SIZE)
                y = (BUFFER_SIZE * (r+1)) + (r * SQUARE_SIZE)
                pygame.draw.rect(self.screen, self.box[r][c].color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                if self.selected == [r, c]:
                    pygame.draw.rect(self.screen, SELECTED_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE), width=SELECTED_WIDTH)
        return

    def draw_screen(self):
        # Base
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw Grid
        self.draw_grid()

        # Update
        pygame.display.flip()
        return

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            # Key Presses
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Quit
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # Reset
                    elif event.key == pygame.K_r:
                        self.box = Box()
                    # Print Box
                    elif event.key == pygame.K_p:
                        self.box.display()
                    # Move Selected
                    elif event.key == pygame.K_LEFT:
                        self.selected[1] = max(0, self.selected[1] - 1)
                    elif event.key == pygame.K_RIGHT:
                        self.selected[1] = min(GRID_SIZE[1], self.selected[1] + 1)
                    elif event.key == pygame.K_UP:
                        self.selected[0] = max(0, self.selected[0] - 1)
                    elif event.key == pygame.K_DOWN:
                        self.selected[0] = min(GRID_SIZE[0], self.selected[0] + 1)
                    # Change Particles
                    elif event.key == pygame.K_s:
                        self.selected_particle = Sand()
                    elif event.key == pygame.K_w:
                        self.selected_particle = Water()
                    # Add Particle
                    elif event.key == pygame.K_SPACE:
                        self.inject()

            # Update
            self.box.tick()
            self.draw_screen()
            # Maintain FPS
            clock.tick(FPS)

        # Close
        pygame.quit()
        return


if __name__ == "__main__":
    w = Window()

