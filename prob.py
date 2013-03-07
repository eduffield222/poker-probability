

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
    community_cards.append (deck.deal())
    community_cards.append (deck.deal())
    community_cards.append (deck.deal())
    community_cards.append (deck.deal())

    my_hand = Hand(community_cards)
    my_hand.add (deck.deal())
    my_hand.add (deck.deal())

    print my_hand.display_cards()
    print "IS FOUR OF A KIND", my_hand.four_of_a_kind()
    print "IS THREE OF A KIND", my_hand.three_of_a_kind()
    print "IS FLUSH", my_hand.is_flush()
    print "IS STRAIGHT", my_hand.is_straight()
    #if my_hand.is_flush(): c += 1
    #if my_hand.is_straight(): c += 1

print "took", time() - start
print "count", c


