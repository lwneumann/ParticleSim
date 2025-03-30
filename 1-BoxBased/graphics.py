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
        self.selected = STARTING_POS
        self.selected_particle = "S"
        self.box = Box()
        self.saves = [Box() for b in range(SAVE_SLOTS)]
        return
    
    def inject(self):
        self.box.replace(self.selected[0], self.selected[1], self.selected_particle)
        return

    def draw_square(self, color, x, y, w=0, size=SQUARE_SIZE):
        pygame.draw.rect(self.screen, color, (x, y, size, size), width=w)
        return

    def draw_grid(self):
        for r in range(GRID_SIZE[0]):
            for c in range(GRID_SIZE[1]):
                x = EDGE_BUFFER + (BUFFER_SIZE * (c+1)) + (c * SQUARE_SIZE)
                y = EDGE_BUFFER + (BUFFER_SIZE * (r+1)) + (r * SQUARE_SIZE)
                self.draw_square(PARTICLE_COLORS[self.box[r][c]], x, y)
                if self.selected == [r, c]:
                    self.draw_square(SELECTED_COLOR, x, y, w=SELECTED_WIDTH)
        return

    def draw_menu(self):
        # Draw Selected
        self.draw_square(PARTICLE_COLORS[self.selected_particle], MENU_X_START, EDGE_BUFFER, size=SELECTED_PREVIEW_SIZE)
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
            # Redo key presses
            # https://stackoverflow.com/questions/72876552/how-do-i-make-hotkeys-in-pygame
            
            # --- Key Presses
            keys = pygame.key.get_pressed()
            # Quit
            if keys[pygame.K_ESCAPE]:
                running = False
            # Reset
            if keys[pygame.K_r]:
                self.box = Box()
            # Print Box
            if keys[pygame.K_p]:
                self.box.display()
            # Move Selected
            if keys[pygame.K_LEFT]:
                self.selected[1] = max(0, self.selected[1] - 1)
            elif keys[pygame.K_RIGHT]:
                self.selected[1] = min(GRID_SIZE[1]-1, self.selected[1] + 1)
            if keys[pygame.K_UP]:
                self.selected[0] = max(0, self.selected[0] - 1)
            elif keys[pygame.K_DOWN]:
                self.selected[0] = min(GRID_SIZE[0]-1, self.selected[0] + 1)
            # Change Particles
            if keys[pygame.K_s]:
                self.selected_particle = "S"
            elif keys[pygame.K_w]:
                self.selected_particle = "W"
            elif keys[pygame.K_a]:
                self.selected_particle = "s"
            elif keys[pygame.K_e]:
                self.selected_particle = "E"
            elif keys[pygame.K_v]:
                self.selected_particle = "V"
            # Save Slots
            if keys[pygame.K_LSHIFT]:
                print(keys)
                if keys[pygame.K_KP1]:
                    self.save(1)
            # Load slots
            else:
                if keys[pygame.K_KP1]:
                    self.load(1)
            # Add Particle
            if keys[pygame.K_SPACE]:
                self.inject()
            # --- Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update
            self.box.tick()
            self.draw_screen()
            # Maintain FPS
            clock.tick(FPS)

        # Close
        pygame.font.quit()
        pygame.quit()
        return


if __name__ == "__main__":
    w = Window()

