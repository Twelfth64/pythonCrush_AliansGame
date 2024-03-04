
class GameStats:
    """Collect statistic about Alien Invasion game."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Game Aliens Invasion starts in active state
        self.game_active = True

    def reset_stats(self):
        """Initioalize statistics duirng a game."""
        self.ships_left = self.settings.ship_limit
