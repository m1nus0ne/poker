class Card(object):
    def __init__(self,suit: Suit, value: Value):
        self.suit = suit
        self.value = value
    def getDesk(self):
        pass
    def __str__(self):
        suits = ['Пики',]