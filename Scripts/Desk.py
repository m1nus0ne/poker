from random import choice
from  Card.Card import Card
class Deck(object):
    def newDeck(self):
        self.deck = [Card[i%4,i//4] for i in range(52)]
    def giveCard(self):
        return choice(self.deck)
