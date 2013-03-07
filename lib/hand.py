
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

        for combo in combos:
            all_preset = True
            for card1 in combo:
                found = False
                for card2 in all_cards:
                    if card1 == card2.kind:
                        found = True
                if not found: all_preset = False
            if all_preset:
                return True

        return False

    def four_of_a_kind(self):
        return self.of_a_kind(4)

    def three_of_a_kind(self):
        return self.of_a_kind(3)

    def one_pair(self):
        return self.of_a_kind(2)

    def of_a_kind(self, needed_count):
        all_cards = self._cards
        all_cards.extend(self._community_cards)

        for kind in ('2', '3', '4', '5',  '6',  '7',  '8',  '9',  'T',  'J',  'Q',  'K',  'A'):
            count = 0

            for i in xrange(len(all_cards)):
                if self._cards[i].kind == kind: count += 1

            if count == needed_count:
                return True

        return False

    def get_highest_kind(self):
        all_cards = self._cards

        highest_kind = 0
        count_kind = 0
        for kind in ('2', '3', '4', '5',  '6',  '7',  '8',  '9',  'T',  'J',  'Q',  'K',  'A'):
            count_kind += 1
            for i in xrange(len(all_cards)):
                if self._cards[i].kind == kind:
                    highest_kind = count_kind

        return highest_kind

    def get_strength(self):
        #royal flush 90
        if self.is_straight() and self.is_flush: return 120 + self.get_highest_kind()
        if self.four_of_a_kind(): return 100 + self.get_highest_kind()
        if self.three_of_a_kind() and self.one_pair(): return 80 + self.get_highest_kind() #full house
        if self.is_flush(): return 80 + self.get_highest_kind()
        if self.is_straight(): return 60 + self.get_highest_kind()
        if self.three_of_a_kind(): return 40 + self.get_highest_kind()
        if self.one_pair(): return 20 + self.get_highest_kind()
        return self.get_highest_kind()

    def __gt__(self, hand1, hand2):
        return hand1.get_strength() > hand2.get_strength()

