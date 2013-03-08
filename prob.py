

import os,sys
sys.path.insert(1, './lib')

from time import time
from deck import Deck
from card import Card
from hand import Hand
from re import split

my_cards1 = None
my_cards2 = None
community_cards1 = None
community_cards2 = None
community_cards3 = None
community_cards4 = None
community_cards5 = None

for stage in range(1, 5):

    if stage == 1:
        cards = raw_input("Enter your cards (7c As): ").upper()
        cards_split = split(' ', cards)
        my_cards1 = Card(cards_split[0][0], cards_split[0][1])
        my_cards2 = Card(cards_split[1][0], cards_split[1][1])
    if stage == 2:
        community = raw_input("Enter first 3 community cards (3s As Ts): ").upper()
        community_split = split(' ', community)
        community_cards1 = Card(community_split[0][0], community_split[0][1])
        community_cards2 = Card(community_split[1][0], community_split[1][1])
        community_cards3 = Card(community_split[2][0], community_split[2][1])
    if stage == 3:
        community = raw_input("Enter next community card (As): ").upper()
        community_split = split(' ', community)
        community_cards4 = Card(community_split[0][0], community_split[0][1])
    if stage == 4:
        community = raw_input("Enter next community card (As): ").upper()
        community_split = split(' ', community)
        community_cards5 = Card(community_split[0][0], community_split[0][1])


    start = time()
    total = 10000.0

    count_my_straights = 0
    count_my_flushes = 0
    count_my_four_of_a_kind = 0
    count_my_three_of_a_kind = 0
    count_my_one_pair = 0
    deck = Deck()

    for i in xrange(int(total)):
        deck.get_new_deck()

        community_cards = []
        community_cards.append (community_cards1 or deck.deal())
        community_cards.append (community_cards2 or deck.deal())
        community_cards.append (community_cards3 or deck.deal())
        community_cards.append (community_cards4 or deck.deal())
        community_cards.append (community_cards5 or deck.deal())

        my_hand = Hand(community_cards)
        my_hand.add (my_cards1)
        my_hand.add (my_cards2)

        if my_hand.is_flush(): count_my_flushes += 1.0
        if my_hand.is_straight(): count_my_straights += 1.0
        if my_hand.three_of_a_kind(): count_my_three_of_a_kind += 1.0
        if my_hand.one_pair(): count_my_one_pair += 1.0

    count_their_straights = 0
    count_their_flushes = 0
    count_their_four_of_a_kind = 0
    count_their_three_of_a_kind = 0
    count_their_one_pair = 0
    deck = Deck()

    for i in xrange(int(total)):
        deck.get_new_deck()

        community_cards = []
        community_cards.append (community_cards1 or deck.deal())
        community_cards.append (community_cards2 or deck.deal())
        community_cards.append (community_cards3 or deck.deal())
        community_cards.append (community_cards4 or deck.deal())
        community_cards.append (community_cards5 or deck.deal())

        my_hand = Hand(community_cards)
        my_hand.add (deck.deal())
        my_hand.add (deck.deal())

        if my_hand.is_flush(): count_their_flushes += 1.0
        if my_hand.is_straight(): count_their_straights += 1.0
        if my_hand.three_of_a_kind(): count_their_three_of_a_kind += 1.0
        if my_hand.one_pair(): count_their_one_pair += 1.0

    print "---------------------------------------------"
    print "took", time() - start
    print "PROBABILITY             YOU   ", "THEM", "RATIO"
    print "count flush          ", round(count_my_flushes / total, 4)        , round(count_their_flushes / total, 4), round( (count_my_flushes / total) / (count_their_flushes / total), 4)
    print "count straight       ", round(count_my_straights / total, 4)      , round(count_their_straights / total, 4), round( (count_my_straights / total) / (count_their_straights / total), 4)
    print "count three_of_a_kind", round(count_my_three_of_a_kind / total, 4), round(count_their_three_of_a_kind / total, 4), round( (count_my_three_of_a_kind / total) / (count_their_three_of_a_kind / total), 4)
    print "count one pair       ", round(count_my_one_pair / total, 4)       , round(count_their_one_pair / total, 4), round( (count_my_one_pair / total) / (count_their_one_pair / total), 4)

