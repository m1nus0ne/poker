from Match import Match
from Player import Player

class GameCommand:
    def __init__(self, player: Player, match: Match):
        self.player = player
        self.match = match

    def ecxecute(self):
        pass