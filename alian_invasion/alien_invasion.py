import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Class representing an Alien Invasion game.
        To control resources and game mechanics"""

    def __init__(self):
        """Initialize game and create game recourcies."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Make game stats instance
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make Play button
        self.play_button = Button(self, "Play")

    def run_game(self) -> None:
        """Start main game loop"""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        # For tracking events of keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Starts new game by pressing Play button"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _check_keydown_events(self, event):
        """Check if key is pressed and update ship accordingly."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Check if key is released and update ship accordingly."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullet and add to group bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullets position and delete bullets that are no longer needed."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Check if bullets hit aliens.If so, delete bullets and aliens."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Create a new fleet of aliens and remove current bullets
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Update positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Check collision between ship and aliens
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        # Check if aliens hit bottom of screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Check if ship hit by alien."""
        if self.stats.ships_left > 0:
            # Decrease ship_left
            self.stats.ships_left -= 1
    
            # Reset aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
    
            # Pause
            sleep(1)
        else:
            self.stats.game_active = False
    
    def _check_aliens_bottom(self):
        """Check if aliens hit bottom of screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    
    def _create_fleet(self):
        """Make fleet of aliens and count them in a row."""
        # Space between alians equal to one alian
        alien = Alien(self)
        alien_width, alian_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Count a number of possible rows at the screen"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alian_height) - ship_height)
        number_rows = available_space_y // (3 * alian_height)

        # Make first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Make alien and add to group aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Check if alien meet edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Change direction of fleet."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update image on screen and display new frame."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Button Play is displayed if game inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Display last frame
        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance and run game
    ai = AlienInvasion()
    ai.run_game()
