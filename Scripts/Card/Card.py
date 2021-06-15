from enum import IntEnum, Enum
class Card(object):
    def __init__(self,suit: Enum, value: Enum):

        self.suit = suit
        self.value = value
    def __str__(self):
       return '{} of {}'.format(self.value.name,self.suit.name)

class Value(Enum):
    two = 0
    three = 1
    four = 2
    five = 3
    six = 4
    seven = 5
    eight = 6
    nine = 7
    ten = 8
    jack = 9
    queen = 10
    king = 11
    ace = 12

class Suit(Enum):
    spades = 0
    clubs = 1
    diamonds = 2
    hearts = 3

