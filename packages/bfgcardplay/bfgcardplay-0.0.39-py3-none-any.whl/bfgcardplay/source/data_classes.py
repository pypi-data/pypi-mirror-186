from termcolor import cprint
from typing import Tuple, List

from bridgeobjects import Card, RANKS


MODULE_COLOUR = 'yellow'


class SuitCards():
    """Represent all of the cards in a suit by name."""
    def __init__(self, suit: str):
        self.suit = suit
        self.ace = Card('A', suit)
        self.king = Card('K', suit)
        self.queen = Card('Q', suit)
        self.jack = Card('J', suit)
        self.ten = Card('T', suit)
        self.nine = Card('9', suit)
        self.eight = Card('8', suit)
        self.seven = Card('7', suit)
        self.six = Card('6', suit)
        self.five = Card('5', suit)
        self.four = Card('4', suit)
        self.three = Card('3', suit)
        self.two = Card('2', suit)

    def cards(self, top_rank: str = '', bottom_rank: str = '') -> Tuple[Card]:
        """Return a tuple of the cards requested."""
        if not top_rank:
            top_rank = 'A'
        if not bottom_rank:
            bottom_rank = '2'

        cards = []
        ranks = [rank for rank in RANKS]
        ranks.reverse()
        ranks = ranks[:-1]
        top_index = ranks.index(top_rank)
        bottom_index = ranks.index(bottom_rank)
        requested_ranks = ranks[top_index:bottom_index+1]
        for rank in requested_ranks:
            cards.append(Card(rank, self.suit))
        return tuple(cards)

    def sorted_cards(self):
        """Return a list of Cards in descending order by rank."""
        ranks = [rank for rank in RANKS]
        ranks.reverse()
        ranks = ranks[:-1]
        cards = []
        for rank in ranks:
            cards.append(Card(rank, self.suit))
        return cards


class CardArray():
    """Data structure for dashboard analyses"""
    def __init__(self, cards: List[Card]):
        self.cards = self.sort_cards(cards)
        self.suits = self._suits_from_cards()

    def _suits_from_cards(self):
        """Return a dict of suit cards."""
        suits = {}
        for card in self.cards:
            suit = card.suit.name
            if suit not in suits:
                suits[suit] = []
            suits[suit].append(card)
        return suits

    @property
    def count(self):
        """Return the length of cards"""
        return len(self.cards)

    def __repr__(self):
        # cprint(f'{self.cards}', MODULE_COLOUR)
        # cprint(f'{self.suits}', MODULE_COLOUR)
        return ''

    @staticmethod
    def sort_cards(cards: List[Card]) -> List[Card]:
        """Return a sorted list of cards."""
        return sorted(cards, reverse=True)
