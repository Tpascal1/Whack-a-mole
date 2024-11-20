import pygame
import random


def main():
    try:
        # Initialize Pygame
        pygame.init()

        # Load the mole image (make sure mole.png is in the same folder)
        mole_image = pygame.image.load("mole.png")

        # Set up the screen size (640x512) and title
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-A-Mole")

        # Initial mole position (randomly placed on the grid)
        mole_x = random.randrange(0, 20)
        mole_y = random.randrange(0, 16)

        # Create a clock object to control the frame rate
        clock = pygame.time.Clock()

        # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position
                    mouse_x, mouse_y = event.pos

                    # Check if the mouse clicked on the mole's grid square
                    mole_rect = pygame.Rect(mole_x * 32, mole_y * 32, 32, 32)
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        # Move the mole to a new random position when clicked
                        mole_x = random.randrange(0, 20)
                        mole_y = random.randrange(0, 16)

            # Fill the screen with a light green background color
            screen.fill("light blue")

            # Draw the grid (20 columns, 16 rows)
            for x in range(0, 640, 32):  # Vertical lines
                pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, 512))
            for y in range(0, 512, 32):  # Horizontal lines
                pygame.draw.line(screen, (255, 255, 255), (0, y), (640, y))

            # Draw the mole at the current position
            screen.blit(mole_image, (mole_x * 32, mole_y * 32))

            # Update the display to show the changes
            pygame.display.flip()

            # Control the frame rate (60 FPS)
            clock.tick(60)

    finally:
        # Quit Pygame when the game loop ends
        pygame.quit()


# Corrected condition to run the game
if __name__ == "__main__":
    main()
