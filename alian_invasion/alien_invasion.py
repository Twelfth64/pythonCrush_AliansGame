import sys

import pygame

from settings import Settings
from ship import Ship


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

        self.ship = Ship(self)

    def run_game(self) -> None:
        """Start main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # For tracking events of keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Check if key is pressed and update ship accordingly."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Check if key is released and update ship accordingly."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update image on screen and display new frame."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Display last frame
        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance and run game
    ai = AlienInvasion()
    ai.run_game()
