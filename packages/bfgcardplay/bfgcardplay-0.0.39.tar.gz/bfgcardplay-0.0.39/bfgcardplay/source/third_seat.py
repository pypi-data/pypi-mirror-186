""" Third seat card play."""

from typing import Tuple

from bridgeobjects import Card, Denomination
from bfgsupport import Trick

from .player import Player


class ThirdSeat():
    def __init__(self, player: Player):
        self.player = player

    @staticmethod
    def _trick_card_values(trick: Trick, trumps: Denomination) -> Tuple[int, int]:
        """Return a tuple of card values."""
        value_0 = trick.cards[0].value
        if trick.cards[1].suit == trick.cards[0].suit:
            value_1 = trick.cards[1].value
        else:
            value_1 = 0
        if trumps:
            if trick.cards[0].suit == trumps:
                value_0 += 13
            if trick.cards[1].suit == trumps:
                value_1 = trick.cards[1].value + 13
        return (value_0, value_1)

    def _ace_is_deprecated(self, trick: Trick, card: Card) -> bool:
        """Return True if the ace is not to be played."""
        player = self.player
        if card.value != 13:
            return False

        king = Card(f'K{card.suit.name}')
        # print(player.card_has_been_played(king), trick.cards[1] == king)
        if self.player.card_has_been_played(king) or trick.cards[1] == king:
            return False

        if len(player.total_unplayed_cards[trick.suit]) < 9:
            return False

        return True

    def _trump_partners_card(self, player: Player, trick: Trick) -> bool:
        """Return True if third hand is to overtump partner's lead."""
        (value_0, value_1) = self._trick_card_values(trick, player.trump_suit)
        opponents_cards = player.opponents_unplayed_cards[trick.suit.name]
        if value_1 > value_0 and trick.cards[0].suit != player.trump_suit:
            return True
        for card in opponents_cards:
            if card.value > trick.cards[0].value:
                return True
        return False

    # def _best_suit(self, player: Player) -> Suit:
    #     """Select suit for signal."""
    #     # TODO handle no points and equal suits
    #     cards = player.hand_cards.list
    #     suit_points = player.get_suit_strength(cards)
    #     max_points = 0
    #     best_suit = None
    #     for suit in SUITS:
    #         hcp = suit_points[suit]
    #         if hcp > max_points:
    #             max_points = hcp
    #             best_suit = suit
    #     if not best_suit:
    #         return player.longest_suit
    #     return Suit(best_suit)
