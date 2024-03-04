class Settings:
    """Class for storing settings of Alian Invasion game."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen params
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship speed
        self.ship_speed = 1

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15