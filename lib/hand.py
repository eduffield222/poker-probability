
from card import Card
from random import randint

class Hand(object):
    def __init__(self, community_cards):
        self._cards = []
        self._community_cards = community_cards

    def add(self, card):
        self._cards.append(card)

    def is_flush(self):
        all_cards = self._cards
        all_cards.extend(self._community_cards)

        for suit in ('h', 's', 'd', 'c'):
            count = 0

            for i in xrange(len(all_cards)):
                if self._cards[i].suit == suit: count += 1

            if count == 5:
                return True

        return False

    def is_straight(self):
        all_cards = []
        all_cards = self._cards
        all_cards.extend(self._community_cards)

        combos = []
        combos.append(['A', '2', '3', '4', '5'])
        combos.append(['2', '3', '4', '5', '6'])
        combos.append(['3', '4', '5', '6', '7'])
        combos.append(['4', '5', '6', '7', '8'])
        combos.append(['5', '6', '7', '8', '9'])
        combos.append(['6', '7', '8', '9', 'T'])
        combos.append(['7', '8', '9', 'T', 'J'])
        combos.append(['8', '9', 'T', 'J', 'Q'])
        combos.append(['9', 'T', 'J', 'Q', 'K'])
        combos.append(['T', 'J', 'Q', 'K', 'A'])


        print all_cards
        return False

        for combo in combos:
            all_preset = True
            for card1 in combo:
                found = False
                print "----------------"
                print all_cards
                for card2 in all_cards:
                    print card1, card2.name
                #    if card1 == card2.name:
                #        found = True
                #if not found: all_preset = False
            if all_preset:
                return True

        return False


    def get_strength(self):
        #royal flush 90
        if self.is_straight() and self.is_flush: return 80
        if self.four_of_a_kind(): return 70
        #full house 60
        if self.is_flush(): return 50
        if self.is_straight(): return 40
        if self.three_of_a_kind(): return 30
        if self.two_pair(): return 20
        if self.one_pair(): return 10
        #highest card value

    def __gt__(self, hand1, hand2):
        pass

