import pygame.font
from pygame.sprite import Group
import json

from ship import Ship

class Scoreboard:
    """A class to report scoring information."""
    def __init__(self,ai_game):
        """Initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats
    
        # Font settings for scoring information.
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        # Prepare the initial score image.
        self._prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def _prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.game_stats.score)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        # display the score at the top of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.game_stats.high_score)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = str(self.game_stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships/lives are left"""
        self.ships = Group()
        for ship_number in range(self.game_stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10  + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        """Check to see if there is a new high score"""
        if self.game_stats.score > self.game_stats.high_score:
            self.game_stats.high_score = self.game_stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def log_highscore(self):
        filename = "highscores.json"
        with open(filename,"w") as scores_file:
            round_highscore = round(self.game_stats.high_score)
            # json_highscore = "{:,}".format(round_highscore)
            # json_highscore = int(json_highscore)
            json.dump(round_highscore,scores_file)