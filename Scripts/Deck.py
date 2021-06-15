from random import shuffle
from Scripts.Card.Card import Card, Value, Suit


class Deck(object):  # static clAss
    def __init__(self):
        self.deck = [Card(Value(i // 4), Suit(i % 4)) for i in range(52)]
        shuffle(self.deck)

    def giveCard(self):
        return self.deck.pop()


