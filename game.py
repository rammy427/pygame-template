import pygame

# Initialize window.
pygame.init()

# screen is a Surface (to render game onto).
# set_mode returns a Surface.
screen = pygame.display.set_mode((800, 600))
screen_rect = pygame.Rect(0, 0, 800, 600)

clock = pygame.time.Clock()

running = True

# Main game loop. Runs 60 times per second.
while running:
    # Poll for events. Iterate through every event in the queue.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with color to clear previous frame.
    screen.fill("black")

    # -------------- UPDATE THE GAME HERE -----------------
    # -----------------------------------------------------
    
    # Flip display to render the new frame.
    pygame.display.flip()

    # Limit framerate to 60 FPS.
    clock.tick(60)

pygame.quit()
