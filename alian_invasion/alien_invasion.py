import sys

import pygame

from settings import Settings


class AlienInvasion:
    """Class representing an Alien Invasion game.
        To control resources and game mechanics"""

    def __init__(self):
        """Initialize game and create game recourcies."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height
             ))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self) -> None:
        """Start main game loop"""
        while True:
            # For tracking events of keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            # Display last frame
            pygame.display.flip()


if __name__ == '__main__':
    # Make game instance and run game
    ai = AlienInvasion()
    ai.run_game()
