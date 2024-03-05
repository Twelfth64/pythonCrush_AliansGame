
class GameStats:
    """Collect statistic about Alien Invasion game."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Game Aliens Invasion starts in inactive state
        self.game_active = False

        # Achievements are not reset
        self.high_score = self.upload_score()

    def reset_stats(self):
        """Initioalize statistics duirng a game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_score(self):
        """Saving highest score"""
        with open('alien_invasion_high_score.txt', 'w') as f:
            f.write(str(self.high_score))

    def upload_score(self):
        """Upload the highest score to high score table."""
        with open('alien_invasion_high_score.txt', 'r') as f:
            self.high_score = int(f.read())
        return self.high_score


