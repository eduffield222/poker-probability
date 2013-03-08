

from sys import path as sys_path, argv, exit
sys_path.insert(1, '../lib/')

import unittest
import logging
from urllib import quote_plus
from time import time, sleep
import unittest
from deck import Deck
from card import Card
from hand import Hand

class TestHands(unittest.TestCase):
    def test_flushes(self):
        deck = Deck()
        deck.get_new_deck()

        community_cards = []
        community_cards.append (Card('T', 's'))
        community_cards.append (Card('3', 's'))
        community_cards.append (Card('8', 's'))
        community_cards.append (deck.deal())
        community_cards.append (deck.deal())

        my_hand = Hand(community_cards)
        my_hand.add (Card('2', 's'))
        my_hand.add (Card('4', 's'))

        assert my_hand.is_flush()

    def test_flushes2(self):
        deck = Deck()
        deck.get_new_deck()

        community_cards = []
        community_cards.append (deck.deal())
        community_cards.append (deck.deal())
        community_cards.append (Card('2', 'd'))
        community_cards.append (Card('3', 'd'))
        community_cards.append (Card('4', 'd'))

        my_hand = Hand(community_cards)
        my_hand.add (Card('T', 'd'))
        my_hand.add (Card('J', 'd'))

        assert my_hand.is_flush()

    def test_straight(self):
        deck = Deck()
        deck.get_new_deck()

        community_cards = []
        community_cards.append (deck.deal())
        community_cards.append (deck.deal())
        community_cards.append (Card('2', 'd'))
        community_cards.append (Card('3', 's'))
        community_cards.append (Card('4', 's'))

        my_hand = Hand(community_cards)
        my_hand.add (Card('5', 'd'))
        my_hand.add (Card('6', 'd'))

        assert my_hand.is_straight()

    def test_straight_flash(self):
        deck = Deck()
        deck.get_new_deck()

        community_cards = []
        community_cards.append (deck.deal())
        community_cards.append (deck.deal())
        community_cards.append (Card('2', 'd'))
        community_cards.append (Card('3', 'd'))
        community_cards.append (Card('4', 'd'))

        my_hand = Hand(community_cards)
        my_hand.add (Card('5', 'd'))
        my_hand.add (Card('6', 'd'))

        assert my_hand.is_straight() and my_hand.is_flush()

    def test_one_pair(self):
        deck = Deck()
        deck.get_new_deck()

        community_cards = []
        community_cards.append (Card('2', 'd'))
        community_cards.append (Card('3', 'd'))
        community_cards.append (Card('4', 'd'))

        my_hand = Hand(community_cards)
        my_hand.add (Card('2', 's'))
        my_hand.add (Card('6', 'd'))

        assert my_hand.one_pair() and not my_hand.is_flush()

    def test_three_of_a_kind(self):
        deck = Deck()
        deck.get_new_deck()

        community_cards = []
        community_cards.append (Card('2', 'd'))
        community_cards.append (Card('2', 'c'))
        community_cards.append (Card('4', 'd'))

        my_hand = Hand(community_cards)
        my_hand.add (Card('2', 's'))
        my_hand.add (Card('6', 'd'))

        assert my_hand.three_of_a_kind() and not my_hand.one_pair()

    def test_full_house(self):
        deck = Deck()
        deck.get_new_deck()

        community_cards = []
        community_cards.append (Card('2', 'd'))
        community_cards.append (Card('2', 'c'))
        community_cards.append (Card('6', 'd'))

        my_hand = Hand(community_cards)
        my_hand.add (Card('2', 's'))
        my_hand.add (Card('6', 'd'))

        assert my_hand.three_of_a_kind() and my_hand.one_pair()

if __name__ == '__main__':
    unittest.main()
