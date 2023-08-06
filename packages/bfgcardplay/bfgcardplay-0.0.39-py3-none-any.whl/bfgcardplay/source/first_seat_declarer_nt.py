# first_seat_declarer_nt.py
""" First seat card play for declarer in NT contracts."""

from typing import List, Union
from termcolor import colored
import random
import inspect

from ..logger import log

from bridgeobjects import SUITS, Card, Suit

import bfgcardplay.source.declarer_play as declarer
import bfgcardplay.source.global_variables as global_vars
from .player import Player, Cards
from .first_seat import FirstSeat
from.declarer_play import card_combinations

MODULE_COLOUR = 'red'


class FirstSeatDeclarerNT(FirstSeat):
    def __init__(self, player: Player):
        super().__init__(player)

    def selected_card(self) -> Card:
        """Return the card for the first seat."""
        player = self.player
        self.update_manager()
        if len(player.hand.unplayed_cards) == 1:
            return log(inspect.stack(), player.hand.unplayed_cards[0])

        # dashboard = player.dashboard
        # threats = dashboard.threats
        # winners = dashboard.winners
        # suit_lengths = dashboard.suit_lengths
        # extra_winners_length = dashboard.extra_winners_length
        # extra_winners_strength = dashboard.extra_winners_strength

        card = self._select_card_from_manager_suit_to_develop()
        if card:
            return card

        # No strategy established yet so select a suit
        suit = self._select_suit()
        card = self._select_lead_card(suit)
        if card:
            return card

        raise ValueError(f'No cards for {suit}')

    def _select_card_from_manager_suit_to_develop(self) -> Card:
        """Return the selected card from suit to develop."""
        player = self.player
        manager = global_vars.manager
        suit_to_develop = manager.suit_to_develop(player.seat)

        if not suit_to_develop:
            return None

        suit_name = suit_to_develop.name
        if player.suit_cards[suit_to_develop]:
            card = card_combinations(player, suit_name)
            # if card:
            return card

        if player.our_unplayed_cards[suit_name]:
            card = self._card_from_suit_to_develop(suit_to_develop)
            if card:
                return card
        else:
            manager.set_suit_to_develop(player.seat, None)
        return None

    def _card_from_suit_to_develop(self, suit_to_develop) -> Card:
        """Return card from suit to develop."""
        player = self.player
        manager = global_vars.manager
        entries = player.get_entries(player.partners_hand)

        if player.suit_cards[suit_to_develop]:
            if manager.suit_strategy(player.seat)[suit_to_develop.name] == 'missing_ace':
                card = declarer.lead_to_find_missing_ace(player, suit_to_develop)
                if card:
                    return card
            elif manager.suit_strategy(player.seat)[suit_to_develop.name] == 'missing_king':
                card = declarer.missing_king(player, suit_to_develop)
                if card:
                    return card
            elif manager.suit_strategy(player.seat)[suit_to_develop.name] == 'missing_queen':
                card = declarer.missing_queen(player, suit_to_develop)
                if card:
                    return card

            if (len(player.suit_cards[suit_to_develop]) == 1 and
                    not player.partners_suit_cards[suit_to_develop]):
                card = player.suit_cards[suit_to_develop][0]
                manager.set_suit_to_develop(player.seat, None)
                return log(inspect.stack(), card)
            elif entries:
                for suit_name, cards in entries.items():
                    if cards:
                        if player.suit_cards[suit_name]:
                            card = player.suit_cards[suit_name][-1]
                            return log(inspect.stack(), card)
        return None

    def _select_suit(self) -> Suit:
        """Return the trick lead suit for the declarer in  a suit contract."""
        player = self.player
        manager = global_vars.manager
        dashboard = player.dashboard

        # Look for suit to develop
        # print(colored(f'{dashboard.tricks_needed=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.sure_tricks.count=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.sure_tricks.cards=}', MODULE_COLOUR))
        # print(colored(f'{player.declarers_tricks=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.probable_tricks.cards=}', MODULE_COLOUR))
        # print(colored(f'{dashboard.possible_tricks.cards=}', MODULE_COLOUR))
        # # print(colored(f'{dashboard.possible_promotions.cards=}', MODULE_COLOUR))

        # Play last winner in case no entry
        tricks_needed = dashboard.tricks_needed - player.declarers_tricks
        if tricks_needed <= dashboard.sure_tricks.count:
            for suit in SUITS:
                opponents_length = len(player.total_unplayed_cards[suit]) - len(player.our_unplayed_cards[suit])
                if opponents_length <= 2:
                    if player.unplayed_cards[suit] and not player.partners_unplayed_cards[suit]:
                        if player.is_winner_declarer(player.unplayed_cards[suit][0]):
                            return log(inspect.stack(), Suit(suit))

        # suit_to_develop has been defined
        suit = manager.suit_to_develop(player.seat)
        if suit:
            if player.unplayed_cards[suit]:
                return log(inspect.stack(), suit)

        # Look for suit to develop
        if dashboard.probable_tricks.count:
            extras_suits = dashboard.probable_tricks.suits
        else:
            extras_suits = dashboard.possible_tricks.suits
        if extras_suits:
            suits = {suit: 0 for suit in SUITS}
            for suit in extras_suits:
                suits[suit] = len(extras_suits[suit])
            best_suit = player.get_list_of_best_scores(suits)
            if len(best_suit) == 1:
                suit = Suit(best_suit[0])
                manager.set_suit_to_develop(player.seat, suit)
                if player.unplayed_cards[suit]:
                    return log(inspect.stack(), suit)

        # This crude logic stops the player cashing their winners early
        suit = self._select_suit_with_winners()
        if suit:
            return suit

        # Develop longer suits as hands develop
        suit = self._develop_suit_as_play_progresses()
        if suit:
            input()
            return suit

        # Find suit, but avoid suit if better for opponents to lead
        suit = self._avoid_suit_with_potential_winner()
        if suit:
            return suit

        # Find a suit to develop
        if not manager.suit_to_develop(player.seat):
            suit_to_develop = self._suit_to_develop()
            if suit_to_develop:
                return log(inspect.stack(), suit_to_develop)

        suit_scores = {suit: 0 for suit in SUITS}
        for suit in SUITS:
            our_cards = Cards(player.our_unplayed_cards[suit])
            suit_scores[suit] += our_cards.value + len(player.our_unplayed_cards[suit])
        suits = player.get_list_of_best_scores(suit_scores)
        if len(suits) == 1:
            return log(inspect.stack(), Suit(suits[0]))

        suit = Suit(random.choice(suits))
        print(colored(f'fsd_nt random.choice(suits) {suits[0]}', MODULE_COLOUR))
        return log(inspect.stack(), suit)

    def _select_suit_with_winners(self):
        """Return"""
        player = self.player
        manager = global_vars.manager

        if len(player.board.tricks) < 4:
            set_strategy_limit = 7
        else:
            set_strategy_limit = 1

        # Play

        winners = {suit: len(player.dashboard.winners[suit]) for suit in SUITS}
        best_suits = player.get_list_of_best_scores(winners)
        for suit in best_suits:
            if (player.dashboard.winners[suit] and
                    player.unplayed_cards[suit] and
                    len(player.our_cards[suit]) >= set_strategy_limit):
                manager.set_suit_strategy(player.seat, suit, 'Play winners')
                return log(inspect.stack(), Suit(suit))
        return None

    def _develop_suit_as_play_progresses(self):
        """Return"""
        player = self.player
        manager = global_vars.manager
        candidate_suits = {}
        if len(player.board.tricks) > 1:
            for suit in SUITS:
                if len(player.unplayed_cards[suit]) >= 4 or len(player.partners_unplayed_cards[suit]) >= 4:
                    points = player.get_suit_strength(player.our_unplayed_cards[suit])
                    candidate_suits[suit] = len(player.our_unplayed_cards[suit]) + points[suit]

            if candidate_suits:
                candidates = player.get_list_of_best_scores(candidate_suits)
                suit = candidates[0]
                manager.set_suit_to_develop(player.seat, Suit(suit))
                for card in player.partners_unplayed_cards[suit]:
                    if card.is_honour and player.is_winner_declarer(card):
                        return log(inspect.stack(), Suit(suit))
        return None

    def _avoid_suit_with_potential_winner(self):
        """Return"""
        player = self.player
        suits = []
        for suit in SUITS:
            if player.unplayed_cards[suit]:
                if not self._potential_winner(suit):
                    suits.append(suit)

        # Must have one suit!
        if not suits:
            for suit in SUITS:
                if player.unplayed_cards[suit]:
                    suits.append(suit)

        if len(suits) == 1:
            return log(inspect.stack(), Suit(suits[0]))
        return None

    def _suit_to_develop(self) -> List[str]:
        """Return a list of suits to develop."""
        player = self.player
        if len(player.board.tricks) > 9:
            return None
        manager = global_vars.manager
        long_suits_to_develop = self._long_suits_to_develop()
        longest_strongest_suit = self._longest_strongest_suit(long_suits_to_develop)
        suit = Suit(longest_strongest_suit)
        manager.set_suit_to_develop(player.seat, suit)
        suit_strategy = self._set_suit_strategy(suit)
        manager.set_suit_strategy(player.seat, suit.name, suit_strategy)
        return suit

    def _set_suit_strategy(self, suit: Suit) -> str:
        """Return the suit strategy as a string."""
        player = self.player

        missing_honours = player.missing_honours(suit)
        for missing_honour in missing_honours:
            if missing_honour.rank == 'A':
                return 'missing_ace'
            if missing_honour.rank == 'K':
                return 'missing_king'
            if missing_honour.rank == 'Q':
                return 'missing_queen'
        return ''

    def _long_suits_to_develop(self):
        """Return a list of long suits to develop."""
        player = self.player
        long_suits_to_develop = []
        for suit_name in SUITS:
            declarers_suit_cards = player.declarers_suit_cards[suit_name]
            dummys_suit_cards = player.dummys_suit_cards[suit_name]
            total_cards = len(declarers_suit_cards) + len(dummys_suit_cards)
            if (total_cards >= 6 and (len(declarers_suit_cards) >= 4 or len(dummys_suit_cards) >= 4)):
                long_suits_to_develop.append(suit_name)
        return long_suits_to_develop

    def _longest_strongest_suit(self, suits: List[str]) -> str:
        """Return the longest and strongest suit from a list of suit_names."""
        player = self.player
        manager = global_vars.manager
        candidate_suits = {}
        for suit_name in suits:
            declarers_suit_cards = player.declarers_suit_cards[suit_name]
            dummys_suit_cards = player.dummys_suit_cards[suit_name]
            candidate_suits[suit_name] = len(declarers_suit_cards) + len(dummys_suit_cards)
        long_suits = player.get_list_of_best_scores(candidate_suits)

        if len(long_suits) == 1:
            suit = long_suits[0]
            manager.set_suit_to_develop(player.seat, suit)
            suit_strategy = self._set_suit_strategy(Suit(suit))
            manager.set_suit_strategy(player.seat, suit, suit_strategy)
            return suit

        strong_suits = player.get_list_of_best_scores(candidate_suits)
        if len(strong_suits) == 1:
            return log(inspect.stack(), strong_suits[0])

        if strong_suits:
            suit = random.choice(strong_suits)
            return log(inspect.stack(), Suit(suit))
        for suit in SUITS:
            if player.dashboard.winners[suit] and player.unplayed_cards[suit]:
                return log(inspect.stack(), suit)

        suits = []
        for suit in SUITS:
            if player.unplayed_cards[suit]:
                suits.append(suit)
        suit = random.choice(suits)
        return suit

    def _select_lead_card(self, suit: Suit) -> Union[Card, None]:
        """Return the selected lead card for declarer."""
        player = self.player
        manager = global_vars.manager
        cards = player.suit_cards[suit.name]
        if not cards:
            return None

        # Card combinations
        card = card_combinations(player, suit.name)
        if card:
            return log(inspect.stack(), card)

        # Play winning cards
        if (manager.suit_strategy(player.seat)[suit.name] == 'Play winners' or
                player.holds_all_winners_in_suit(suit)):
            my_cards = player.unplayed_cards[suit.name]
            partners_cards = player.partners_unplayed_cards[suit.name]
            if (partners_cards and len(my_cards) > len(partners_cards) and
                    player.is_winner_declarer(partners_cards[0])):
                return log(inspect.stack(), my_cards[-1])
            for card in cards[::-1]:
                if player.opponents_unplayed_cards[suit.name]:
                    if player.is_winner_declarer(card):
                        return log(inspect.stack(), card)
                else:
                    return log(inspect.stack(), card)

        # Top of touching honours
        for index, card in enumerate(cards[:-1]):
            if card.is_honour and card.value == cards[index+1].value + 1:
                return log(inspect.stack(), card)

        # Top of doubleton
        if len(cards) == 2:
            return log(inspect.stack(), cards[0])

        # Return bottom card
        return log(inspect.stack(), cards[-1])

    def _potential_winner(self, suit: str) -> bool:
        """Return True if the suit has a potential winner."""
        player = self.player
        for cards in [player.unplayed_cards[suit], player.partners_unplayed_cards[suit]]:
            if (cards and
                    cards[0] != player.total_unplayed_cards[suit][0] and
                    cards[0] == player.total_unplayed_cards[suit][1] and
                    len(cards) >= 2):
                return True
        return False
