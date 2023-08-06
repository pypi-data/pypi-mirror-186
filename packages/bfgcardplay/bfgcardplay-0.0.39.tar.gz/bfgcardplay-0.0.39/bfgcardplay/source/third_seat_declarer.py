"""Third seat card play for declarer."""

from typing import Union, Dict
from termcolor import colored

from bridgeobjects import SUITS, Card, Suit
from bfgsupport import Trick

import inspect

from ..logger import log

import bfgcardplay.source.global_variables as global_vars
from .player import Player, SuitCards
from .third_seat import ThirdSeat
from .declarer_play import card_combinations

MODULE_COLOUR = 'blue'


class ThirdSeatDeclarer(ThirdSeat):
    def __init__(self, player: Player):
        super().__init__(player)

    def selected_card(self) -> Card:
        """Return the card if the third seat."""
        player = self.player
        trick = player.board.tricks[-1]
        manager = global_vars.manager

        cards = player.cards_for_trick_suit(trick)

        # Void
        if not cards:
            return self._select_card_if_void(player, trick)

        # Singleton
        if len(cards) == 1:
            return log(inspect.stack(), cards[0])

        # Choice of card has already been made
        if manager.card_to_play[player.seat]:
            card = manager.card_to_play[player.seat]
            manager.card_to_play[player.seat] = None
            return log(inspect.stack(), card)

        # This is a suit to develop
        suit_to_develop = manager.suit_to_develop(player.seat)
        if (suit_to_develop and
                suit_to_develop == trick.suit and
                player.suit_cards[suit_to_develop]):
            card = self._select_card_in_suit_to_develop(suit_to_develop, trick)
            return card

        # Win trick if possible
        winning_card = self._get_winning_card(player, trick)
        if winning_card:
            return winning_card

        # Cover honour with honour
        if trick.cards[1].is_honour and trick.cards[1].value > trick.cards[0].value:
            for card in cards[::-1]:
                if card.value > trick.cards[1].value:
                    return log(inspect.stack(), card)

        return log(inspect.stack(), cards[-1])

    def _select_card_in_suit_to_develop(self, suit: Suit, trick: Trick) -> Card:
        """Return the card from a suit to develop."""
        player = self.player
        dashboard = player.dashboard
        manager = global_vars.manager
        cards = player.suit_cards[suit.name]
        (ace, king, queen, jack) = SuitCards(suit.name).cards('A', 'J')

        missing_king = manager.missing_king[player.seat][suit.name]

        if manager.win_trick[player.seat]:
            manager.win_trick[player.seat] = False
            for card in cards[::-1]:
                if card.value > player.opponents_unplayed_cards[suit.name][0].value:
                    return log(inspect.stack(), card)

        if manager.suit_strategy(player.seat)[suit.name] == 'missing_ace':
            if not trick.cards[0].is_honour:
                for card in cards:
                    if card.is_honour:
                        return log(inspect.stack(), card)

        if player.holds_all_winners_in_suit(suit, trick):
            return log(inspect.stack(), cards[0])

        if missing_king:
            if ace in cards and queen not in cards:
                return log(inspect.stack(), ace)
        if manager.suit_strategy(player.seat)[suit.name] == 'missing_king':
            if trick.cards[0] == queen or trick.cards[0] == jack:
                return log(inspect.stack(), cards[-1])

        missing_queen = queen in player.opponents_unplayed_cards[suit.name]
        if manager.suit_strategy(player.seat)[suit.name] == 'missing_queen' and missing_queen:
            card = self._get_winning_card(player, trick)
            if card:
                return card

        # Play top card if winner and suit nearly played out
        if dashboard.sure_tricks.count == 13 - player.trick_number:
            for card in cards[::-1]:
                if player.is_winner_declarer(card, trick):
                    return log(inspect.stack(), card)

        if (cards[0].is_honour and
                cards[0].value == cards[1].value + 1 and
                cards[1].value > trick.cards[1].value):
            return log(inspect.stack(), cards[1])

        if player.is_tenace(cards[0], cards[1]) and missing_king:
            return log(inspect.stack(), cards[1])

        # Force out honour
        if len(cards) > 1 and len(player.opponents_unplayed_cards[suit]) > 1:
            if (cards[1].value > player.opponents_unplayed_cards[suit][1].value and
                    cards[1].value > trick.cards[1].value):
                return log(inspect.stack(), cards[1])

        # Play winner if needed to make contract
        tricks_needed = dashboard.tricks_needed - player.declarers_tricks
        if tricks_needed <= dashboard.sure_tricks.count:
            if player.is_winner_declarer(cards[0], trick):
                return log(inspect.stack(), cards[0])

        if len(player.opponents_unplayed_cards[suit]) == 1:
            for card in cards[::-1]:
                if player.is_winner_declarer(card, trick):
                    return log(inspect.stack(), card)

        if len(player.partners_unplayed_cards[suit.name]) < len(player.unplayed_cards[suit.name]):
            return log(inspect.stack(), cards[-1])

        if not player.is_winner_declarer(trick.cards[0], trick):
            for index, card in enumerate(cards[:-1]):
                if card.value > trick.cards[1].value and card. value > cards[index+1].value + 1:
                    return log(inspect.stack(), card)

        return log(inspect.stack(), cards[-1])

    def _get_winning_card(self, player: Player, trick: Trick) -> Union[Card, None]:
        """Return a card if it can win the trick."""
        cards = player.cards_for_trick_suit(trick)
        dashboard = player.dashboard

        # Trick cards
        value_0, value_1 = player.card_value(trick.cards[0]), player.card_value(trick.cards[1])

        # Look for tenace about a threat card and play lower card
        (higher_card, lower_card) = player.card_from_my_tenace()
        if (lower_card and
                lower_card.value > value_0 and
                lower_card.value > value_1):
            return log(inspect.stack(), lower_card)

        # Is this a suit to develop?
        manager = global_vars.manager
        if (manager.suit_to_develop(player.seat) == trick.suit or
                manager.suit_strategy(player.seat)[trick.suit.name] == 'missing_queen'):
            opponents_cards = player.opponents_unplayed_cards[trick.suit.name]
            tenace_in_my_hand = player.get_suit_tenaces(cards)
            if tenace_in_my_hand:
                for card in cards:
                    if card.value < tenace_in_my_hand.value:
                        return log(inspect.stack(), card)
            else:
                for card in cards[::-1]:
                    if card.value > value_0 + 1 and card.value > opponents_cards[0].value:
                        return log(inspect.stack(), card)

        # If we hold all the winners, take the trick
        if (player.holds_all_winners_in_suit(trick.suit, trick) or
                dashboard.sure_tricks.count >= 13 - player.trick_number):
            if player.opponents_unplayed_cards[trick.suit]:
                if (trick.cards[0].value > player.opponents_unplayed_cards[trick.suit][0].value and
                        trick.cards[0].value > trick.cards[1].value):
                    return log(inspect.stack(), cards[-1])
                else:
                    return log(inspect.stack(), cards[0])

        # If we probably hold all the winners, take the trick
        if player.holds_all_winners_in_suit(trick.suit, trick):
            if player.opponents_unplayed_cards[trick.suit]:
                if (trick.cards[0].value > player.opponents_unplayed_cards[trick.suit][0].value and
                        trick.cards[0].value > trick.cards[1].value):
                    return log(inspect.stack(), cards[-1])
                else:
                    return log(inspect.stack(), cards[0])

        # Take finesse
        # for card in cards:
        card = card_combinations(player)
        if card:
            return log(inspect.stack(), card)

        top_in_tenace = player.get_suit_tenaces(player.our_unplayed_cards[trick.suit.name])
        if top_in_tenace:
            for card in cards:
                if card.value < top_in_tenace.value + 1:
                    return log(inspect.stack(), card)

        # Win trick if possible to de-block suit
        if trick.cards[0].value < cards[0].value:
            # value_0, value_1 = player.card_value(trick.cards[0]), player.card_value(trick.cards[1])
            is_winner = player.is_winner_declarer(trick.cards[0], trick) and value_0 > value_1
            if is_winner and len(player.partners_unplayed_cards[trick.suit.name]) > 1:
                return log(inspect.stack(), cards[-1])
            our_cards = player.our_unplayed_cards[trick.suit.name]
            partners_length = len(player.partners_unplayed_cards[trick.suit.name])
            my_length = len(player.unplayed_cards[trick.suit.name])
            if (player.is_winner_declarer(our_cards[0], trick) and
                    player.is_winner_declarer(our_cards[1], trick) and
                    my_length < partners_length):
                return log(inspect.stack(), cards[0])

        # Cover honour with honour
        if trick.cards[1].is_honour and trick.cards[1].value > trick.cards[0].value:
            for card in cards[::-1]:
                if card.value > trick.cards[0].value and card.value > trick.cards[1].value:
                    return log(inspect.stack(), card)

        # Push out honour
        if cards[0].is_honour and not player.is_winner_declarer(cards[0]) and len(cards) > 1:
            return log(inspect.stack(), cards[1])

        # Overtake partner if appropriate
        if not player.is_winner_declarer(trick.cards[0], trick):
            for index, card in enumerate(cards[:-1]):
                card_value = card.value
                # trick card values already adjusted for trumps
                if card.suit == player.trump_suit:
                    card_value += 13

                if (card_value > value_0 + 1 and
                        card_value > value_1 and
                        card.value != cards[index+1].value + 1):
                    if not self._ace_is_deprecated(trick, card):
                        return log(inspect.stack(), card)

        # Play winner
        if not player.is_winner_declarer(trick.cards[0], trick):
            for card in cards[::-1]:
                if player.is_winner_declarer(card, trick):
                    return log(inspect.stack(), card)

        # Play bottom card if no other information
        if cards[-1].value > value_0 and cards[-1].value > value_1:
            return log(inspect.stack(), cards[-1])

        return None

    def _select_card_if_void(self, player: Player, trick: Trick) -> Card:
        """Return card if cannot follow suit."""
        player.record_void(trick.suit)

        # Trump if appropriate
        if player.trump_suit:
            if not player.is_winner_declarer(trick.cards[0], trick):
                opponents_trumps = player.opponents_unplayed_cards[player.trump_suit.name]
                if player.trump_cards and not opponents_trumps:
                    return log(inspect.stack(), player.trump_cards[-1])
                if player.trump_cards and opponents_trumps:
                    if self._trump_partners_card(player, trick):
                        card_value = trick.cards[1].value
                        if trick.cards[1].suit == player.trump_suit:
                            card_value += 13
                        trump_cards = player.unplayed_cards[player.trump_suit]
                        for card in trump_cards[::-1]:
                            if card.value + 13 > card_value:
                                return log(inspect.stack(), card)

        opponents_cards = player.opponents_unplayed_cards[trick.suit.name]

        # Find card to discard
        if player.trump_suit:
            suits = {suit_name: suit for suit_name, suit in SUITS.items() if suit_name != player.trump_suit.name}
        else:
            suits = {suit_name: suit for suit_name, suit in SUITS.items()}

        # print(colored(f'{dashboard.tricks_needed=}', MODULE_COLOUR))
        # print(colored(f'{player.declarers_tricks=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.sure_tricks.count=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.probable_tricks.count=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.possible_tricks.count=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.sure_tricks.cards=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.probable_tricks.cards=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.possible_promotions.cards=}', MODULE_COLOUR))

        # Find a loser
        suit_length: Dict[str, int] = {}
        for suit_name, suit in suits.items():
            if player.suit_cards[suit_name]:
                suit_length[suit_name] = len(player.suit_cards[suit_name])
                our_cards = player.our_unplayed_cards[suit_name]
                opponents_cards = player.opponents_unplayed_cards[suit_name]
                # print(colored(f'{suit} {len(opponents_cards)}', MODULE_COLOUR))
                if opponents_cards:
                    if (our_cards[0].value < opponents_cards[0].value and
                            len(player.unplayed_cards[suit_name]) > len(opponents_cards) / 2):
                        return log(inspect.stack(), player.suit_cards[suit_name][-1])
                else:
                    return log(inspect.stack(), player.suit_cards[suit_name][-1])

        # Only trumps left
        if not suit_length:
            return log(inspect.stack(), player.trump_cards[-1])

        # Return smallest in longest suit
        # TODO we might not want to do this
        sorted_suit_length = {
            key: value for key, value in sorted(suit_length.items(),
                                                key=lambda item: item[1], reverse=True)
            }
        long_suit = list(sorted_suit_length)[0]
        return log(inspect.stack(), player.suit_cards[long_suit][-1])
