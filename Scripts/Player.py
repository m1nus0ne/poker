from Scripts.Card.Card import Card
class Player(object):
    def __init__(self, hand: list, name: str):
        self.hand = hand
        self.name = name
    def addCard(self,card: Card):
        self.hand += card
        
