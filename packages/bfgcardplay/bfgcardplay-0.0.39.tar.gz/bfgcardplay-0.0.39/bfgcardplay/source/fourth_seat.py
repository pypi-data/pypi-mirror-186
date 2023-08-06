"""Fourth seat card play."""
from typing import List, Union, Tuple

import inspect
from ..logger import log

from bridgeobjects import Card, Denomination
from bfgsupport import Trick
from .player import Player


class FourthSeat():
    def __init__(self, player: Player):
        self.player = player

    def _winning_card(self, trick: Trick) -> Union[Card, None]:
        """Return the card if can win trick."""
        player = self.player
        cards = self.player.cards_for_trick_suit(trick)

        (value_0, value_1, value_2) = self._trick_card_values(trick, player.trump_suit)
        if cards:
            for card in cards[::-1]:
                card_value = card.value
                if card.suit == player.trump_suit:
                    card_value += 13
                if card_value > value_0 and card_value > value_2:
                    log(inspect.stack(), f'{card}')
                    return card

        # No cards in trick suit, look for trump winner
        elif player.trump_cards:
            for card in player.trump_cards[::-1]:
                if card.value + 13 > value_2:
                    log(inspect.stack(), f'{card}')
                    return card
        return None

    def _second_player_winning_trick(self, cards: List[Card], trick: Trick, trumps: Denomination) -> bool:
        """Return True if the second player is winning the trick."""
        (value_0, value_1, value_2) = self._trick_card_values(trick, trumps)
        if value_1 > value_0 and value_1 > value_2:
            return True
        return False

    @staticmethod
    def _trick_card_values(trick: Trick, trumps: Denomination) -> Tuple[int, int, int]:
        """Return a tuple of card values."""
        value_0 = trick.cards[0].value
        if trick.cards[1].suit == trick.cards[0].suit:
            value_1 = trick.cards[1].value
        else:
            value_1 = 0
        if trick.cards[2].suit == trick.cards[0].suit:
            value_2 = trick.cards[2].value
        else:
            value_2 = 0
        if trumps:
            if trick.cards[0].suit == trumps:
                value_0 += 13
            if trick.cards[1].suit == trumps:
                value_1 = trick.cards[1].value + 13
            if trick.cards[2].suit == trumps:
                value_2 = trick.cards[2].value + 13
        return (value_0, value_1, value_2)

    def can_win_trick(self, player, card) -> bool:
        """Return True if card can win trick."""
        trick = player.board.tricks[-1]
        trumps = player.trump_suit
        (value_0, value_1, value_2) = self._trick_card_values(trick, trumps)
        if value_1 > value_0 and value_1 > value_2:
            return False
        if card.value > value_0 and card.value > value_2:
            return True
        return False
