class Settings:
    """Class for storing settings of Alian Invasion game."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen params
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship speed
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15

        # Settings aliens
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 - means right, -1 - means left
        self.fleet_direction = 1
