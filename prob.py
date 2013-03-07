

import os,sys
sys.path.insert(1, './lib')

from time import time
from deck import Deck
from card import Card
from hand import Hand
from re import split

deck = Deck()

cards =  raw_input("Enter your cards (7c As): ")
community = raw_input("Enter first 3 community cards (3s As Ts): ")

cards_split = split(' ', cards)
community_split = split(' ', community)

start = time()
total = 10000.0
count_straights = 0
count_flushes = 0
count_four_of_a_kind = 0
count_three_of_a_kind = 0
count_one_pair = 0

for i in xrange(int(total)):
    deck.get_new_deck()

    community_cards = []
    community_cards.append (Card(community_split[0][0], community_split[0][1]))
    community_cards.append (Card(community_split[1][0], community_split[1][1]))
    community_cards.append (Card(community_split[2][0], community_split[2][1]))
    community_cards.append (deck.deal())
    community_cards.append (deck.deal())

    my_hand = Hand(community_cards)
    my_hand.add (Card(cards_split[0][0], cards_split[0][1]))
    my_hand.add (Card(cards_split[1][0], cards_split[1][1]))

    #print my_hand.display_cards()
    #print "IS FOUR OF A KIND", my_hand.four_of_a_kind()
    #print "IS THREE OF A KIND", my_hand.three_of_a_kind()
    #print "IS FLUSH", my_hand.is_flush()
    #print "IS STRAIGHT", my_hand.is_straight()

    if my_hand.is_flush(): count_flushes += 1.0
    if my_hand.is_straight(): count_straights += 1.0
    if my_hand.three_of_a_kind(): count_three_of_a_kind += 1.0
    if my_hand.one_pair(): count_one_pair += 1.0

print "took", time() - start
print "count flush", count_flushes / total
print "count straight", count_straights / total
print "count three_of_a_kind", count_three_of_a_kind / total
print "count one pair", count_one_pair / total


