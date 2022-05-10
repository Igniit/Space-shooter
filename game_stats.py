import json


class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game in an active state.
        self.game_active = False

        # High score is stored in a json and read from.
        filename = "highscores.json"
        with open(filename) as highscore:
            high_score = json.load(highscore)
        self.high_score = int(high_score)

        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0


