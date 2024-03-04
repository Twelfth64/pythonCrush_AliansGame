import pygame


class Ship:
    """Class to design ships for the game."""

    def __init__(self, ai_game):
        """Initialize ship and set it start position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Upload ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # Each new ship is placed at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Saving float coordinate of the ship
        self.x = float(self.rect.x)

        # Moving flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= 1

        self.rect.x = self.x

    def blitme(self):
        """Draw a ship in current position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Set ship in the center of the bottom of screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
