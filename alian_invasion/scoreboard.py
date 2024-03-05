import pygame.font


class Scoreboard:
    """Class to display game score."""

    def __init__(self, ai_game):
        """Initialize the scoreboard attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Set font for scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare original image
        self.prep_score()

    def prep_score(self):
        """Make image from current score."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                            self.text_color, self.settings.bg_color)

        # Display score in top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Display score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
