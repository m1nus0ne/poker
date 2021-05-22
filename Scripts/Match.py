from Round import Round


class Match(object):
    def __init__(self, dillerId: int, currentRound: Round, table: list, players: list, deck: list):
        self.players = players
        self.currentRound = currentRound
        self.table = table
        self.dillerId = dillerId
        self.deck = deck

    def startMatch(self):

