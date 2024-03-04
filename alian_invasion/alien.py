import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class, representing an alien invasion ship."""

    def __init__(self, ai_game):
        """Initialize the alien, and set it start position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Upload alien image and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Each new alien has a left top corner position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save horizontal alien position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien to the right or left"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
