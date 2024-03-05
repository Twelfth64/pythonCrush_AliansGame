class Settings:
    """Class for storing settings of Alian Invasion game."""

    def __init__(self):
        """Initialize static game settings."""
        # Screen params
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

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

        # Speedup scale
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings, changable during the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1

        # fleet_direction = 1 - means right, -1 - means left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed of game."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale