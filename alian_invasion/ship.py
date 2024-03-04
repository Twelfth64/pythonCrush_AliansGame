import pygame


class Ship:
    """Class to design ships for the game."""

    def __init__(self, ai_game):
        """Initialize ship and set it start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Upload ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # Each new ship is placed at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw a ship in current position."""
        self.screen.blit(self.image, self.rect)
