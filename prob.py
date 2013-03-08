

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
    count_my_hand_strength = 0
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
        if my_hand.four_of_a_kind(): count_my_four_of_a_kind += 1.0
        if my_hand.three_of_a_kind(): count_my_three_of_a_kind += 1.0
        if my_hand.one_pair(): count_my_one_pair += 1.0
        count_my_hand_strength += my_hand.get_strength()

    count_their_straights = 0
    count_their_flushes = 0
    count_their_four_of_a_kind = 0
    count_their_three_of_a_kind = 0
    count_their_one_pair = 0
    count_their_hand_strength = 0
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
        if my_hand.four_of_a_kind(): count_their_four_of_a_kind += 1.0
        if my_hand.three_of_a_kind(): count_their_three_of_a_kind += 1.0
        if my_hand.one_pair(): count_their_one_pair += 1.0
        count_their_hand_strength += my_hand.get_strength()

    print "---------------------------------------------"
    print "took", time() - start
    print "PROBABILITY             YOU   ", "THEM", "RATIO"

    ratio_flush, ratio_straight, ratio_four_of_a_kind, ratio_three_of_a_kind = 1,1,1,1

    try:
        my_flush = round(count_my_flushes / total, 4)
        their_flush = round(count_their_flushes / total, 4)
        ratio_flush = my_flush / their_flush
        print "count flush          ", my_flush, their_flush, ratio_flush
    except:
        raise

    try:
        my_straight = round(count_my_straights / total, 4)
        their_straight = round(count_their_straights / total, 4)
        ratio_straight = my_straight / their_straight
        print "count straight          ", my_straight, their_straight, ratio_straight
    except:
        raise

    try:
        my_four_of_a_kind = round(count_my_four_of_a_kind / total, 4)
        their_four_of_a_kind = round(count_their_four_of_a_kind / total, 4)
        ratio_four_of_a_kind = my_four_of_a_kind / their_four_of_a_kind
        print "count four_of_a_kind          ", my_four_of_a_kind, their_four_of_a_kind, ratio_four_of_a_kind
    except:
        raise

    try:
        my_three_of_a_kind = round(count_my_three_of_a_kind / total, 4)
        their_three_of_a_kind = round(count_their_three_of_a_kind / total, 4)
        ratio_three_of_a_kind = my_three_of_a_kind / their_three_of_a_kind
        print "count three_of_a_kind          ", my_three_of_a_kind, their_three_of_a_kind, ratio_three_of_a_kind
    except:
        raise

    print "TOTAL HAND STRENGTH", count_my_hand_strength, count_their_hand_strength, round(float(count_my_hand_strength) / float(count_their_hand_strength), 4)