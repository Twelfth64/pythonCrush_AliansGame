import pygame
from pygame.sprite import Sprite


class Alian(Sprite):
    """Class, represeting an alian invasion ship."""

    def __init__(self, ai_game):
        """Initialize the alian, and set it start position."""
        super().__init__()
        self.screen = ai_game.screen

        # Upload alian image and set rect attribute
        self.image = pygame.image.load('images/alian.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Each new alian has a left top corner position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save horizontal alian position
        self.x = float(self.rect.x)