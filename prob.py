

import os,sys
sys.path.insert(1, './lib')

from time import time
from deck import Deck
from card import Card
from hand import Hand

deck = Deck()

start = time()
c = 0
for i in xrange(10000):
    deck.get_new_deck()
    community_cards = []
    my_hand = Hand(community_cards)

    my_hand.add (deck.deal())
    my_hand.add (deck.deal())

    community_cards.append (deck.deal())
    community_cards.append (deck.deal())
    community_cards.append (deck.deal())
    community_cards.append (deck.deal())

    print my_hand.get_strength()
    #if my_hand.is_flush(): c += 1
    #if my_hand.is_straight(): c += 1

print "took", time() - start
print "count", c


