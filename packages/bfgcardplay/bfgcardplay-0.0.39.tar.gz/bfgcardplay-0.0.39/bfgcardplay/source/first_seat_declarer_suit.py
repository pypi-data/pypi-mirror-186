# first_seat_declarer.py
""" First seat card play for declarer."""

from typing import List, Dict, Tuple
from termcolor import cprint

import inspect
from ..logger import log

from bridgeobjects import SUITS, Card, Suit

import bfgcardplay.source.global_variables as global_vars
from .player import Player
from .first_seat import FirstSeat
from .declarer_play import card_combinations

ALL_WINNERS = 5

MODULE_COLOUR = 'cyan'


def return_and_print(obj: object, text: str, can_print: bool) -> object:
    """Print text and return object."""
    if can_print:
        cprint(f'{obj} {text}', MODULE_COLOUR)
    return obj


class FirstSeatDeclarerSuit(FirstSeat):
    def __init__(self, player: Player):
        super().__init__(player)

    def selected_card(self) -> Card:
        """Return the card for the first seat."""
        player = self.player
        dashboard = player.dashboard

        if len(player.hand.unplayed_cards) == 1:
            return log(inspect.stack(), player.hand.unplayed_cards[0])

        # +1 because the next trick has already been created
        if dashboard.winner_count >= 13 - len(player.board.tricks) + 1:
            card = self._play_all_winners()
            if card:
                return card

        manager = global_vars.manager
        self.update_manager()
        suit = self._select_suit()

        if manager.card_to_play[player.seat]:
            card = manager.card_to_play[player.seat][0]
            manager.card_to_play[player.seat].pop(0)
            if manager.suit_to_develop(player.seat) and manager.card_to_play[player.seat]:
                manager.card_to_play[player.seat] = player.suit_cards[manager.suit_to_develop][-1]
            return log(inspect.stack(), card)

        suit_to_develop = manager.suit_to_develop(player.seat)
        if suit_to_develop:
            if player.unplayed_cards[suit_to_develop.name]:
                if manager.suit_strategy(player.seat)[suit_to_develop.name] == 'ruff_in_short_hand':
                    if player.dashboard.threats[suit_to_develop.name]:
                        if player.is_declarer:
                            my_cards = player.unplayed_cards[suit_to_develop.name]
                            dummys_cards = player.dummys_unplayed_cards[suit_to_develop.name]
                            if dummys_cards and dummys_cards[0].value > my_cards[0].value:
                                return log(inspect.stack(), my_cards[-1])
                        card = player.unplayed_cards[suit_to_develop.name][0]
                        return log(inspect.stack(), card)

        if not player.suit_cards[suit.name]:
            raise ValueError(f'No cards for {suit}')
        card = self._select_lead_card(suit)
        return card

    def _select_suit(self) -> Suit:
        """Return the trick lead suit for the declarer in  a suit contract."""
        player = self.player
        dashboard = player.dashboard
        # print(dashboard)
        manager = global_vars.manager
        controls = player.get_controls()
        score_reasons = {}

        # Draw trumps?
        can_draw_trumps = self._can_draw_trumps()
        if player.opponents_trumps and can_draw_trumps:
            return log(inspect.stack(), player.trump_suit)

        # Suit to develop
        suit_to_develop = manager.suit_to_develop(player.seat)
        if suit_to_develop and player.unplayed_cards[suit_to_develop]:
            return log(inspect.stack(), suit_to_develop)
        else:
            # Holds all winners
            for suit_name, suit in SUITS.items():
                if suit != player.trump_suit:
                    if player.holds_all_winners_in_suit(suit):
                        manager.set_suit_to_develop(player.seat, suit)

        # Play master
        if not player.opponents_trumps:
            total_cards = 0
            for suit in SUITS:
                holding = player.unplayed_cards[suit]
                total_cards += len(holding)
            if len(player.unplayed_cards[player.trump_suit]) > total_cards - 2:
                return log(inspect.stack(), player.trump_suit)

            for suit in SUITS:
                if suit != player.trump_suit.name and player.unplayed_cards[suit]:
                    if player.is_winner_declarer(player.unplayed_cards[suit][0]):
                        return log(inspect.stack(), Suit(suit))

        # Long suits
        long_suits = player.partnership_long_suits()
        for suit in long_suits:
            if not self._frozen_suit(suit) and player.can_lead_toward_tenace(suit):
                return log(inspect.stack(), Suit(suit))

        for suit, threat_cards in dashboard.threats.items():
            ace = Card('A', suit)
            king = Card('K', suit)
            queen = Card('Q', suit)
            if len(threat_cards) == 1:
                threat = threat_cards[0]
                if threat == ace and king in player.unplayed_cards[suit]:
                    manager.set_suit_to_develop(player.seat, Suit(suit))
                    manager.set_suit_strategy(player.seat, suit, 'missing_ace')
                elif threat == king and ace in player.unplayed_cards[suit]:
                    manager.set_suit_to_develop(player.seat, Suit(suit))
                    manager.set_suit_strategy(player.seat, suit, 'missing_king')
                elif threat == queen and king in player.unplayed_cards[suit]:
                    manager.set_suit_to_develop(player.seat, Suit(suit))
                    manager.set_suit_strategy(player.seat, suit, 'missing_queen')

        score_reasons['trumps'] = self._deprecate_trumps()

        # print(colored(f'{manager.voids[player.seat]}', MODULE_COLOUR))

        suit_to_develop = manager.suit_to_develop(player.seat)
        if suit_to_develop and player.unplayed_cards[suit_to_develop.name]:
            return log(inspect.stack(), suit_to_develop)

        winners = self._all_winners_score()
        total_winners = 0
        for suit_count in winners:
            total_winners += suit_count[1]
        if total_winners <= 13 - player.trick_number:
            score_reasons['shortage'] = self._shortage_score(controls)
            suit = manager.suit_to_develop(player.seat)
            if suit:
                suit_name = suit.name
                if suit_name and player.suit_cards[suit_name]:
                    return log(inspect.stack(), manager.suit_to_develop(player.seat))
                if not player.suit_cards[suit_name]:
                    manager.set_suit_to_develop(player.seat, None)

        # winning_suit = self._use_winning_suit()
        # if winning_suit:
        #     return winning_suit

        if not player.opponents_trumps:
            long_suits = player.partnership_long_suits()
            for suit in long_suits:
                if not self._frozen_suit(suit) and player.can_lead_toward_tenace(suit):
                    return log(inspect.stack(), Suit(suit))

        for suit in SUITS:
            can_lead_to_dummy = (player.touching_honours_in_hand(player.dummys_hand, suit) and
                                 player.unplayed_cards[suit])
            if player.touching_honours_in_hand(player.hand, suit) or can_lead_to_dummy:
                return log(inspect.stack(), Suit(suit))

        # Look for void in partner's hand
        if player.partners_unplayed_cards[player.trump_suit.name]:
            for suit in SUITS:
                if player.unplayed_cards[suit] and not player.partners_unplayed_cards[suit]:
                    return log(inspect.stack(), Suit(suit))

        # Deprecate voids
        score_reasons['void'] = self._deprecate_suits()

        # All cards are winners
        score_reasons['all_winners'] = self._all_winners_score()

        # Avoid frozen suits
        score_reasons['frozen'] = self._frozen_suits()

        # Long suits
        score_reasons['long'] = self._long_suits()

        # # Short suits
        # score_reasons['short'] = self._short_suits()

        # Select best suit
        best_suit = self._best_suit(score_reasons)
        # print(colored(f'{best_suit=} {score_reasons=}', 'red'))
        return log(inspect.stack(), best_suit)

    def _select_lead_card(self, suit: Suit) -> Card:
        """Return the selected lead card for declarer."""
        player = self.player
        my_cards = player.unplayed_cards[suit.name]
        partners_cards = player.partners_unplayed_cards[suit.name]
        partner_long = len(partners_cards) > len(my_cards)

        # Lead low to partner's winner
        if not partner_long and partners_cards and player.is_winner_declarer(partners_cards[0]):
            return log(inspect.stack(), my_cards[-1])

        # if my_cards and not partner_long:
        #     for card in my_cards[len(partners_cards)-1::-1]:
        #         if player.is_winner_declarer(card):
        #             return log(inspect.stack(), card)

        if player.is_winner_declarer(my_cards[0]) and not player.partners_unplayed_cards[suit.name]:
            return log(inspect.stack(), my_cards[0])

        # Top of touching honours
        for index, card in enumerate(my_cards[:-1]):
            if card.is_honour and card.value == my_cards[index+1].value + 1:
                return log(inspect.stack(), card)

        # Top of doubleton
        if len(my_cards) == 2:
            return log(inspect.stack(), my_cards[0])

        # Card combinations
        card = card_combinations(player, suit.name)
        if card:
            return log(inspect.stack(), card)

        # Winners
        for card in my_cards[::-1]:
            if player.is_winner_declarer(card):
                return log(inspect.stack(), card)

        # Return bottom card
        return log(inspect.stack(), my_cards[-1])

    def _get_winning_suit(self) -> Suit:
        """Return the selected winning suit."""
        player = self.player
        winning_suits = self._get_winning_suit_list()

        long_suits = player.get_list_of_best_scores(winning_suits)
        if long_suits and player.unplayed_cards[long_suits[0]]:
            return log(inspect.stack(), Suit(long_suits[0]))
        return None

    def _get_winning_suit_list(self) -> List[Suit]:
        """Return a list of winning suits."""
        player = self.player
        winning_suits = {}
        for suit_name, suit in SUITS.items():
            our_cards = player.our_unplayed_cards[suit.name]
            if suit != player.trump_suit and our_cards:
                my_cards = player.unplayed_cards[suit_name]
                partners_cards = player.partners_unplayed_cards[suit_name]

                last_card = max(len(my_cards), len(partners_cards)) - 1
                opponents_cards = player.opponents_unplayed_cards[suit.name]
                for index, card in enumerate(our_cards[:last_card]):
                    if index < len(opponents_cards):
                        if card.value < opponents_cards[index].value:
                            break
                else:
                    winning_suits[suit_name] = last_card
        return winning_suits

    def _can_draw_trumps(self) -> Tuple[bool, bool]:
        """Return True if declarer should draw trumps, and/or True to ruff in shorthand."""
        show_return = 0
        player = self.player
        if not player.opponents_unplayed_cards[player.trump_suit.name]:
            return return_and_print(False, 'can_draw_trumps z', show_return)
        if not player.trump_cards:
            return return_and_print(False, 'can_draw_trumps a', show_return)

        if self._ruff_in_short_hand():
            return return_and_print(False, 'can_draw_trumps b', show_return)

        # declarers_trumps = Cards(player.declarers_hand.cards).by_suit[player.trump_suit]
        # dummys_trumps = Cards(player.dummys_hand.cards).by_suit[player.trump_suit]
        # if len(declarers_trumps) + len(dummys_trumps) <= 7 and max(len(declarers_trumps), len(dummys_trumps)) == 4:
        #     return return_and_print(False, 'can_draw_trumps c', show_return)

        # declarers_trumps = player.get_unplayed_cards_by_suit(player.trump_suit, player.declarer)
        # dummys_trumps = player.get_unplayed_cards_by_suit(player.trump_suit, player.dummy)
        our_trumps = player.our_unplayed_cards[player.trump_suit]
        if len(our_trumps) >= 9:  # TODO too simplistic - determine losers first
            return return_and_print(True, 'can_draw_trumps d', show_return)

        # short_hand = player.hands[player.short_suit_seat]
        # print(colored(f'{short_hand}', MODULE_COLOUR))
        # if short_hand.shape[3] <= 2:
        #     # Are there sufficient trumps in short hand?
        #     opponents_trumps = player.opponents_unplayed_cards[player.trump_suit.name]
        #     if len(short_hand.cards_by_suit[player.trump_suit.name]) > len(opponents_trumps):
        #         return return_and_print(True, 'can_draw_trumps e', show_return)
        #     # can declarer produce a void in time?
        #     suit = short_hand.shortest_suit
        #     our_cards = player.our_unplayed_cards[suit]

        #     ace = Card('A', suit.name)
        #     king = Card('K', suit.name)
        #     if ((ace in player.total_unplayed_cards[suit.name] and ace not in our_cards) and
        #             (king in player.total_unplayed_cards[suit.name] and king not in our_cards)):
        #         return return_and_print(False, 'can_draw_trumps f', show_return)
        return return_and_print(True, 'can_draw_trumps g', show_return)

    def _play_all_winners(self) -> Card:
        """Return a card to play when all are winners"""
        player = self.player

        # Draw trumps
        if player.trump_suit:
            suit_name = player.trump_suit.name
            if player.unplayed_cards[suit_name] and player.opponents_unplayed_cards[suit_name]:
                return self._select_card_from_right_hand(suit_name)
        for suit_name, suit in SUITS.items():
            if player.trump_suit and suit == player.trump_suit:
                continue
            if player.unplayed_cards[suit_name]:
                if player.holds_all_winners_in_suit(suit):
                    return self._select_card_from_right_hand(suit_name)
        return None

    def _select_card_from_right_hand(self, suit_name: str) -> Card:
        """Return the appropriate card depending on suit length."""
        player = self.player
        my_cards = player.unplayed_cards[suit_name]
        partners_cards = player.partners_unplayed_cards[suit_name]
        if (partners_cards and
                len(my_cards) < len(partners_cards) and
                my_cards[-1].value < partners_cards[0].value):
            return log(inspect.stack(), player.unplayed_cards[suit_name][0])
        else:
            for card in my_cards[::-1]:
                if player.is_winner_declarer(card):
                    return log(inspect.stack(), card)
        return log(inspect.stack(), player.unplayed_cards[suit_name][-1])

    def _ruff_in_short_hand(self):
        """Update manager if can ruff in short hand and return True."""
        player = self.player
        manager = global_vars.manager

        (long_trump_hand, short_trump_hand) = player.dashboard.get_long_short_trump_hands()
        entries = player.get_entries(long_trump_hand)
        total_entries = 0
        for suit in SUITS:
            if suit != player.trump_suit.name:
                total_entries += len(entries[suit])
        if not total_entries:
            return False

        if not player.partners_unplayed_cards[player.trump_suit.name]:
            return False

        for suit in SUITS:
            (long_hand, short_hand) = player.dashboard.get_long_short_hands(Suit(suit))
            long_cards = long_hand.cards_by_suit[suit]
            short_cards = short_hand.cards_by_suit[suit]
            if (short_cards and
                    len(short_cards) <= 2 and
                    suit != player.trump_suit.name and
                    long_hand == long_trump_hand):
                if ((Card('A', suit) in long_cards and
                        not short_cards[0].is_honour) or
                        Card('A', suit) in short_cards):
                    manager.set_suit_strategy(player.seat, suit, 'ruff_in_short_hand')
                    manager.set_suit_to_develop(player.seat, Suit(suit))
                    if not player.dashboard.threats[suit]:
                        return False
                    # if not player.is_winner_declarer(player.unplayed_cards[suit][-1]):
                    #     print(colored(f'{suit} {player.unplayed_cards[suit]}', MODULE_COLOUR))
                    return True
        return False

    def _long_suits(self) -> List[Tuple[str, int]]:
        """Assign score to suits based on length (long)."""
        player = self.player
        suit_scores = {suit_name: 0 for suit_name in SUITS}
        length_score = self.LENGTH_SCORE

        for suit in SUITS:
            number_cards = len(player.our_cards[suit]) - len(player.opponents_cards[suit])
            if number_cards > 0:
                if player.trump_suit:
                    if suit == player.trump_suit.name:
                        length_score = 0
                suit_scores[suit] = number_cards * length_score
        return [(suit_name, score) for suit_name, score in suit_scores.items()]

    def _all_winners_score(self) -> List[Tuple[str, int]]:
        """Assign score to a suit if all the cards are winners."""
        player = self.player
        suit_scores = {suit_name: 0 for suit_name, suit in SUITS.items()}
        for suit_name, suit in SUITS.items():
            if suit != player.trump_suit:
                if player.holds_all_winners_in_suit(suit):
                    suit_scores[suit_name] = ALL_WINNERS
        return [(suit_name, score) for suit_name, score in suit_scores.items()]

    def _deprecate_trumps(self) -> List[Tuple[str, int]]:
        """Assign score to a suit if opponents have no trumps."""
        suit_scores = {suit_name: 0 for suit_name, suit in SUITS.items()}
        suit_scores[self.player.trump_suit.name] = -1 * self.TRUMP_SCORE
        return [(suit_name, score) for suit_name, score in suit_scores.items()]

    def _suit_strength(self) -> List[Tuple[str, int]]:
        """Assign score to a suit by HCP."""
        suit_scores = {suit_name: 0 for suit_name, suit in SUITS.items()}
        for suit_name in SUITS:
            cards = self.player.our_cards[suit_name]
            for card in cards:
                if card.value >= 10:
                    suit_scores[suit_name] += card.value - 9
        return [(suit_name, score) for suit_name, score in suit_scores.items()]

    def _shortage_score(self, controls: Dict[str, int]) -> List[Tuple[str, int]]:
        """Assign score to a suit if we can create a shortage."""
        player = self.player
        manager = global_vars.manager
        my_trumps = player.unplayed_cards[player.trump_suit]
        partners_trumps = player.unplayed_cards[player.trump_suit]

        suit_scores = {suit_name: 0 for suit_name in SUITS}
        for suit in SUITS:
            if suit != player.trump_suit.name:
                my_cards = player.unplayed_cards[suit]
                partners_cards = player.partners_unplayed_cards[suit]
                if len(my_cards) != len(partners_cards):
                    if ((len(my_cards) > len(partners_cards) and
                            len(partners_trumps) < len(my_trumps)) or
                            (len(my_cards) < len(partners_cards) and
                             len(my_trumps) < len(partners_trumps))):

                        if controls[suit] - len(player.partners_suit_cards[suit]) <= 1:
                            suit_scores[suit] += self.SHORTAGE_SCORE
                            manager.set_suit_to_develop(player.declarer, Suit(suit))
        return [(suit_name, score) for suit_name, score in suit_scores.items()]# first_seat_declarer.py
""" First seat card play for declarer."""

from typing import List, Dict, Tuple
from termcolor import cprint

import inspect
from ..logger import log

from bridgeobjects import SUITS, Card, Suit

import bfgcardplay.source.global_variables as global_vars
from .player import Player
from .first_seat import FirstSeat
from .declarer_play import card_combinations

ALL_WINNERS = 5

MODULE_COLOUR = 'cyan'


def return_and_print(obj: object, text: str, can_print: bool) -> object:
    """Print text and return object."""
    if can_print:
        cprint(f'{obj} {text}', MODULE_COLOUR)
    return obj


class FirstSeatDeclarerSuit(FirstSeat):
    def __init__(self, player: Player):
        super().__init__(player)

    def selected_card(self) -> Card:
        """Return the card for the first seat."""
        player = self.player
        dashboard = player.dashboard

        if len(player.hand.unplayed_cards) == 1:
            return log(inspect.stack(), player.hand.unplayed_cards[0])

        # +1 because the next trick has already been created
        if dashboard.winner_count >= 13 - len(player.board.tricks) + 1:
            card = self._play_all_winners()
            if card:
                return card

        manager = global_vars.manager
        self.update_manager()
        suit = self._select_suit()

        if manager.card_to_play[player.seat]:
            card = manager.card_to_play[player.seat][0]
            manager.card_to_play[player.seat].pop(0)
            if manager.suit_to_develop(player.seat) and manager.card_to_play[player.seat]:
                manager.card_to_play[player.seat] = player.suit_cards[manager.suit_to_develop][-1]
            return log(inspect.stack(), card)

        suit_to_develop = manager.suit_to_develop(player.seat)
        if suit_to_develop:
            if player.unplayed_cards[suit_to_develop.name]:
                if manager.suit_strategy(player.seat)[suit_to_develop.name] == 'ruff_in_short_hand':
                    if player.dashboard.threats[suit_to_develop.name]:
                        if player.is_declarer:
                            my_cards = player.unplayed_cards[suit_to_develop.name]
                            dummys_cards = player.dummys_unplayed_cards[suit_to_develop.name]
                            if dummys_cards and dummys_cards[0].value > my_cards[0].value:
                                return log(inspect.stack(), my_cards[-1])
                        card = player.unplayed_cards[suit_to_develop.name][0]
                        return log(inspect.stack(), card)

        if not player.suit_cards[suit.name]:
            raise ValueError(f'No cards for {suit}')
        card = self._select_lead_card(suit)
        return card

    def _select_suit(self) -> Suit:
        """Return the trick lead suit for the declarer in  a suit contract."""
        player = self.player
        dashboard = player.dashboard
        # print(dashboard)
        manager = global_vars.manager
        controls = player.get_controls()
        score_reasons = {}

        # Draw trumps?
        can_draw_trumps = self._can_draw_trumps()
        if player.opponents_trumps and can_draw_trumps:
            return log(inspect.stack(), player.trump_suit)

        # Suit to develop
        suit_to_develop = manager.suit_to_develop(player.seat)
        if suit_to_develop and player.unplayed_cards[suit_to_develop]:
            return log(inspect.stack(), suit_to_develop)
        else:
            # Holds all winners
            for suit_name, suit in SUITS.items():
                if suit != player.trump_suit:
                    if player.holds_all_winners_in_suit(suit):
                        manager.set_suit_to_develop(player.seat, suit)

        # Play master
        if not player.opponents_trumps:
            total_cards = 0
            for suit in SUITS:
                holding = player.unplayed_cards[suit]
                total_cards += len(holding)
            if len(player.unplayed_cards[player.trump_suit]) > total_cards - 2:
                return log(inspect.stack(), player.trump_suit)

            for suit in SUITS:
                if suit != player.trump_suit.name and player.unplayed_cards[suit]:
                    if player.is_winner_declarer(player.unplayed_cards[suit][0]):
                        return log(inspect.stack(), Suit(suit))

        # Long suits
        long_suits = player.partnership_long_suits()
        for suit in long_suits:
            if not self._frozen_suit(suit) and player.can_lead_toward_tenace(suit):
                return log(inspect.stack(), Suit(suit))

        for suit, threat_cards in dashboard.threats.items():
            ace = Card('A', suit)
            king = Card('K', suit)
            queen = Card('Q', suit)
            if len(threat_cards) == 1:
                threat = threat_cards[0]
                if threat == ace and king in player.unplayed_cards[suit]:
                    manager.set_suit_to_develop(player.seat, Suit(suit))
                    manager.set_suit_strategy(player.seat, suit, 'missing_ace')
                elif threat == king and ace in player.unplayed_cards[suit]:
                    manager.set_suit_to_develop(player.seat, Suit(suit))
                    manager.set_suit_strategy(player.seat, suit, 'missing_king')
                elif threat == queen and king in player.unplayed_cards[suit]:
                    manager.set_suit_to_develop(player.seat, Suit(suit))
                    manager.set_suit_strategy(player.seat, suit, 'missing_queen')

        score_reasons['trumps'] = self._deprecate_trumps()

        # print(colored(f'{manager.voids[player.seat]}', MODULE_COLOUR))

        suit_to_develop = manager.suit_to_develop(player.seat)
        if suit_to_develop and player.unplayed_cards[suit_to_develop.name]:
            return log(inspect.stack(), suit_to_develop)

        winners = self._all_winners_score()
        total_winners = 0
        for suit_count in winners:
            total_winners += suit_count[1]
        if total_winners <= 13 - player.trick_number:
            score_reasons['shortage'] = self._shortage_score(controls)
            suit = manager.suit_to_develop(player.seat)
            if suit:
                suit_name = suit.name
                if suit_name and player.suit_cards[suit_name]:
                    return log(inspect.stack(), manager.suit_to_develop(player.seat))
                if not player.suit_cards[suit_name]:
                    manager.set_suit_to_develop(player.seat, None)

        # winning_suit = self._use_winning_suit()
        # if winning_suit:
        #     return winning_suit

        if not player.opponents_trumps:
            long_suits = player.partnership_long_suits()
            for suit in long_suits:
                if not self._frozen_suit(suit) and player.can_lead_toward_tenace(suit):
                    return log(inspect.stack(), Suit(suit))

        for suit in SUITS:
            can_lead_to_dummy = (player.touching_honours_in_hand(player.dummys_hand, suit) and
                                 player.unplayed_cards[suit])
            if player.touching_honours_in_hand(player.hand, suit) or can_lead_to_dummy:
                return log(inspect.stack(), Suit(suit))

        # Look for void in partner's hand
        if player.partners_unplayed_cards[player.trump_suit.name]:
            for suit in SUITS:
                if player.unplayed_cards[suit] and not player.partners_unplayed_cards[suit]:
                    return log(inspect.stack(), Suit(suit))

        # Deprecate voids
        score_reasons['void'] = self._deprecate_suits()

        # All cards are winners
        score_reasons['all_winners'] = self._all_winners_score()

        # Avoid frozen suits
        score_reasons['frozen'] = self._frozen_suits()

        # Long suits
        score_reasons['long'] = self._long_suits()

        # # Short suits
        # score_reasons['short'] = self._short_suits()

        # Select best suit
        best_suit = self._best_suit(score_reasons)
        # print(colored(f'{best_suit=} {score_reasons=}', 'red'))
        return log(inspect.stack(), best_suit)

    def _select_lead_card(self, suit: Suit) -> Card:
        """Return the selected lead card for declarer."""
        player = self.player
        my_cards = player.unplayed_cards[suit.name]
        partners_cards = player.partners_unplayed_cards[suit.name]
        partner_long = len(partners_cards) > len(my_cards)

        # Lead low to partner's winner
        if not partner_long and partners_cards and player.is_winner_declarer(partners_cards[0]):
            return log(inspect.stack(), my_cards[-1])

        # if my_cards and not partner_long:
        #     for card in my_cards[len(partners_cards)-1::-1]:
        #         if player.is_winner_declarer(card):
        #             return log(inspect.stack(), card)

        if player.is_winner_declarer(my_cards[0]) and not player.partners_unplayed_cards[suit.name]:
            return log(inspect.stack(), my_cards[0])

        # Top of touching honours
        for index, card in enumerate(my_cards[:-1]):
            if card.is_honour and card.value == my_cards[index+1].value + 1:
                return log(inspect.stack(), card)

        # Top of doubleton
        if len(my_cards) == 2:
            return log(inspect.stack(), my_cards[0])

        # Card combinations
        card = card_combinations(player, suit.name)
        if card:
            return log(inspect.stack(), card)

        # Winners
        for card in my_cards[::-1]:
            if player.is_winner_declarer(card):
                return log(inspect.stack(), card)

        # Return bottom card
        return log(inspect.stack(), my_cards[-1])

    def _get_winning_suit(self) -> Suit:
        """Return the selected winning suit."""
        player = self.player
        winning_suits = self._get_winning_suit_list()

        long_suits = player.get_list_of_best_scores(winning_suits)
        if long_suits and player.unplayed_cards[long_suits[0]]:
            return log(inspect.stack(), Suit(long_suits[0]))
        return None

    def _get_winning_suit_list(self) -> List[Suit]:
        """Return a list of winning suits."""
        player = self.player
        winning_suits = {}
        for suit_name, suit in SUITS.items():
            our_cards = player.our_unplayed_cards[suit.name]
            if suit != player.trump_suit and our_cards:
                my_cards = player.unplayed_cards[suit_name]
                partners_cards = player.partners_unplayed_cards[suit_name]

                last_card = max(len(my_cards), len(partners_cards)) - 1
                opponents_cards = player.opponents_unplayed_cards[suit.name]
                for index, card in enumerate(our_cards[:last_card]):
                    if index < len(opponents_cards):
                        if card.value < opponents_cards[index].value:
                            break
                else:
                    winning_suits[suit_name] = last_card
        return winning_suits

    def _can_draw_trumps(self) -> Tuple[bool, bool]:
        """Return True if declarer should draw trumps, and/or True to ruff in shorthand."""
        show_return = 0
        player = self.player
        if not player.opponents_unplayed_cards[player.trump_suit.name]:
            return return_and_print(False, 'can_draw_trumps z', show_return)
        if not player.trump_cards:
            return return_and_print(False, 'can_draw_trumps a', show_return)

        if self._ruff_in_short_hand():
            return return_and_print(False, 'can_draw_trumps b', show_return)

        # declarers_trumps = Cards(player.declarers_hand.cards).by_suit[player.trump_suit]
        # dummys_trumps = Cards(player.dummys_hand.cards).by_suit[player.trump_suit]
        # if len(declarers_trumps) + len(dummys_trumps) <= 7 and max(len(declarers_trumps), len(dummys_trumps)) == 4:
        #     return return_and_print(False, 'can_draw_trumps c', show_return)

        # declarers_trumps = player.get_unplayed_cards_by_suit(player.trump_suit, player.declarer)
        # dummys_trumps = player.get_unplayed_cards_by_suit(player.trump_suit, player.dummy)
        our_trumps = player.our_unplayed_cards[player.trump_suit]
        if len(our_trumps) >= 9:  # TODO too simplistic - determine losers first
            return return_and_print(True, 'can_draw_trumps d', show_return)

        # short_hand = player.hands[player.short_suit_seat]
        # print(colored(f'{short_hand}', MODULE_COLOUR))
        # if short_hand.shape[3] <= 2:
        #     # Are there sufficient trumps in short hand?
        #     opponents_trumps = player.opponents_unplayed_cards[player.trump_suit.name]
        #     if len(short_hand.cards_by_suit[player.trump_suit.name]) > len(opponents_trumps):
        #         return return_and_print(True, 'can_draw_trumps e', show_return)
        #     # can declarer produce a void in time?
        #     suit = short_hand.shortest_suit
        #     our_cards = player.our_unplayed_cards[suit]

        #     ace = Card('A', suit.name)
        #     king = Card('K', suit.name)
        #     if ((ace in player.total_unplayed_cards[suit.name] and ace not in our_cards) and
        #             (king in player.total_unplayed_cards[suit.name] and king not in our_cards)):
        #         return return_and_print(False, 'can_draw_trumps f', show_return)
        return return_and_print(True, 'can_draw_trumps g', show_return)

    def _play_all_winners(self) -> Card:
        """Return a card to play when all are winners"""
        player = self.player

        # Draw trumps
        if player.trump_suit:
            suit_name = player.trump_suit.name
            if player.unplayed_cards[suit_name] and player.opponents_unplayed_cards[suit_name]:
                return self._select_card_from_right_hand(suit_name)
        for suit_name, suit in SUITS.items():
            if player.trump_suit and suit == player.trump_suit:
                continue
            if player.unplayed_cards[suit_name]:
                if player.holds_all_winners_in_suit(suit):
                    return self._select_card_from_right_hand(suit_name)
        return None

    def _select_card_from_right_hand(self, suit_name: str) -> Card:
        """Return the appropriate card depending on suit length."""
        player = self.player
        my_cards = player.unplayed_cards[suit_name]
        partners_cards = player.partners_unplayed_cards[suit_name]
        if (partners_cards and
                len(my_cards) < len(partners_cards) and
                my_cards[-1].value < partners_cards[0].value):
            return log(inspect.stack(), player.unplayed_cards[suit_name][0])
        else:
            for card in my_cards[::-1]:
                if player.is_winner_declarer(card):
                    return log(inspect.stack(), card)
        return log(inspect.stack(), player.unplayed_cards[suit_name][-1])

    def _ruff_in_short_hand(self):
        """Update manager if can ruff in short hand and return True."""
        player = self.player
        manager = global_vars.manager

        (long_trump_hand, short_trump_hand) = player.dashboard.get_long_short_trump_hands()
        entries = player.get_entries(long_trump_hand)
        total_entries = 0
        for suit in SUITS:
            if suit != player.trump_suit.name:
                total_entries += len(entries[suit])
        if not total_entries:
            return False

        if not player.partners_unplayed_cards[player.trump_suit.name]:
            return False

        for suit in SUITS:
            (long_hand, short_hand) = player.dashboard.get_long_short_hands(Suit(suit))
            long_cards = long_hand.cards_by_suit[suit]
            short_cards = short_hand.cards_by_suit[suit]
            if (short_cards and
                    len(short_cards) <= 2 and
                    suit != player.trump_suit.name and
                    long_hand == long_trump_hand):
                if ((Card('A', suit) in long_cards and
                        not short_cards[0].is_honour) or
                        Card('A', suit) in short_cards):
                    manager.set_suit_strategy(player.seat, suit, 'ruff_in_short_hand')
                    manager.set_suit_to_develop(player.seat, Suit(suit))
                    if not player.dashboard.threats[suit]:
                        return False
                    # if not player.is_winner_declarer(player.unplayed_cards[suit][-1]):
                    #     print(colored(f'{suit} {player.unplayed_cards[suit]}', MODULE_COLOUR))
                    return True
        return False

    def _long_suits(self) -> List[Tuple[str, int]]:
        """Assign score to suits based on length (long)."""
        player = self.player
        suit_scores = {suit_name: 0 for suit_name in SUITS}
        length_score = self.LENGTH_SCORE

        for suit in SUITS:
            number_cards = len(player.our_cards[suit]) - len(player.opponents_cards[suit])
            if number_cards > 0:
                if player.trump_suit:
                    if suit == player.trump_suit.name:
                        length_score = 0
                suit_scores[suit] = number_cards * length_score
        return [(suit_name, score) for suit_name, score in suit_scores.items()]

    def _all_winners_score(self) -> List[Tuple[str, int]]:
        """Assign score to a suit if all the cards are winners."""
        player = self.player
        suit_scores = {suit_name: 0 for suit_name, suit in SUITS.items()}
        for suit_name, suit in SUITS.items():
            if suit != player.trump_suit:
                if player.holds_all_winners_in_suit(suit):
                    suit_scores[suit_name] = ALL_WINNERS
        return [(suit_name, score) for suit_name, score in suit_scores.items()]

    def _deprecate_trumps(self) -> List[Tuple[str, int]]:
        """Assign score to a suit if opponents have no trumps."""
        suit_scores = {suit_name: 0 for suit_name, suit in SUITS.items()}
        suit_scores[self.player.trump_suit.name] = -1 * self.TRUMP_SCORE
        return [(suit_name, score) for suit_name, score in suit_scores.items()]

    def _suit_strength(self) -> List[Tuple[str, int]]:
        """Assign score to a suit by HCP."""
        suit_scores = {suit_name: 0 for suit_name, suit in SUITS.items()}
        for suit_name in SUITS:
            cards = self.player.our_cards[suit_name]
            for card in cards:
                if card.value >= 10:
                    suit_scores[suit_name] += card.value - 9
        return [(suit_name, score) for suit_name, score in suit_scores.items()]

    def _shortage_score(self, controls: Dict[str, int]) -> List[Tuple[str, int]]:
        """Assign score to a suit if we can create a shortage."""
        player = self.player
        manager = global_vars.manager
        my_trumps = player.unplayed_cards[player.trump_suit]
        partners_trumps = player.unplayed_cards[player.trump_suit]

        suit_scores = {suit_name: 0 for suit_name in SUITS}
        for suit in SUITS:
            if suit != player.trump_suit.name:
                my_cards = player.unplayed_cards[suit]
                partners_cards = player.partners_unplayed_cards[suit]
                if len(my_cards) != len(partners_cards):
                    if ((len(my_cards) > len(partners_cards) and
                            len(partners_trumps) < len(my_trumps)) or
                            (len(my_cards) < len(partners_cards) and
                             len(my_trumps) < len(partners_trumps))):

                        if controls[suit] - len(player.partners_suit_cards[suit]) <= 1:
                            suit_scores[suit] += self.SHORTAGE_SCORE
                            manager.set_suit_to_develop(player.declarer, Suit(suit))
        return [(suit_name, score) for suit_name, score in suit_scores.items()]
