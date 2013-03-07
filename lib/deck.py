
from card import Card
from random import randint

class Deck(object):
    def __init__(self):
        self._cards = []
        self.get_new_deck()

    def get_new_deck(self):
        self._cards = []
        for name in ('2', '3', '4', '5',  '6',  '7',  '8',  '9',  'T',  'J',  'Q',  'K',  'A'):
            for suit in ('h', 's', 'd', 'c'):
                self._cards.append(Card(name, suit))

    def deal(self):
        return self._cards.pop(randint(0, len(self._cards)-1))