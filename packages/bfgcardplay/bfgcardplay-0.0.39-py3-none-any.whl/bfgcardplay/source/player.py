"""Common functionality for cardplay."""

# from types import List
from termcolor import colored

from typing import List, Dict, Tuple, Union
import random

from bridgeobjects import Suit, Card, SEATS, SUITS, CARD_VALUES
from bfgsupport import Hand, Trick

import bfgcardplay.source.global_variables as global_vars
from .dashboard import Dashboard
from .data_classes import SuitCards

global_vars.initialize()

MODULE_COLOUR = 'magenta'


class Cards():
    """A class representing a set of cards."""
    def __init__(self, input: Union[List[str], List[Card], Hand]):
        self.list = []
        self.longest_suit = None
        by_suit = {suit: [] for key, suit in SUITS.items()}
        by_suit_name = {key: [] for key, suit in SUITS.items()}
        self.by_suit = {**by_suit, **by_suit_name}
        self._value = 0
        self._create(input)

    def count(self) -> int:
        """Return the number of cards."""
        return len(self.list)

    def _create(self, input: Union[List[str], List[Card], Hand]):
        """Create a set of cards"""
        if isinstance(input, Hand):
            cards = input.cards
        elif not isinstance(input, list):
            raise TypeError('Cards must be a list of cards')
        else:
            cards = input

        raw_list = []
        for card in cards:
            if isinstance(card, str):
                card = Card(card)
            raw_list.append(card)
        self.list = self.sort_cards(raw_list)

        self._value = 0
        for card in self.list:
            suit = card.suit
            suit_name = suit.name
            self.by_suit[suit].append(card)
            self.by_suit[suit_name].append(card)
            self._value += card.value
        self.longest_suit = self._longest_suit()

    @staticmethod
    def sort_cards(cards: List[Card]) -> List[Card]:
        """Return a sorted list of cards."""
        return sorted(cards, reverse=True)

    def _longest_suit(self) -> Suit:
        """Return the suit with most cards."""
        suit_dict = {}
        for suit, card_list in self.by_suit.items():
            if isinstance(suit, Suit):
                suit_dict[suit] = len(card_list)
        suits = Player.get_list_of_best_scores(suit_dict)
        suit = random.choice(suits)
        return suit

    @property
    def value(self) -> int:
        """Return the sum of the values of the cards."""
        return self._value


class Player():
    """Object to represent the player: their hand and memory (synonym for Board)."""
    def __init__(self, board):
        self.board = board
        self.dashboard = None

        # Seats and roles
        self.seat = self._get_seat()
        self.seat_index = SEATS.index(self.seat)
        self.partner_seat = self.get_partners_seat(self.seat)
        self.declarer = board.contract.declarer
        self.declarer_index = SEATS.index(self.declarer)
        self.is_declarer = self.seat == self.declarer
        self.dummy_index = (self.declarer_index + 2) % 4
        self.dummy = SEATS[self.dummy_index]
        self.is_dummy = self.seat == self.dummy
        self.is_defender = not (self.is_declarer or self.is_dummy)
        (self.right_hand_seat, self.left_hand_seat) = self._get_opponents_seats()
        self.short_suit_seat = None

        # Hands suits and cards
        self.trump_suit = self._get_trump_suit()
        self.hands = board.hands
        self.hand = board.hands[self.seat]
        self.declarers_hand = board.hands[self.declarer]
        self.dummys_hand = board.hands[self.dummy]

        # self.hand_cards is the Cards object for unplayed cards
        self.hand_cards = Cards(board.hands[self.seat].unplayed_cards)
        self.suit_cards = self.hand_cards.by_suit
        self.unplayed_cards = self.hand_cards.by_suit

        # self.longest_suit = self.hand_cards.longest_suit
        self.longest_suit = self._longest_suit()

        our_cards = Cards(board.hands[self.seat].cards + board.hands[self.partner_seat].cards)
        our_unplayed_cards = Cards(board.hands[self.seat].unplayed_cards + board.hands[self.partner_seat].unplayed_cards)
        self.our_cards: Dict[str, List[Card]] = our_cards.by_suit
        self.our_unplayed_cards: Dict[str, List[Card]] = our_unplayed_cards.by_suit

        opponents_seats = (SEATS[(self.seat_index + 1) % 4], SEATS[(self.seat_index + 3) % 4])
        opponents_cards = Cards(board.hands[opponents_seats[0]].cards + board.hands[opponents_seats[1]].cards)
        opponents_unplayed_cards = Cards(board.hands[opponents_seats[0]].unplayed_cards +
                                         board.hands[opponents_seats[1]].unplayed_cards)
        self.opponents_cards: Dict[str, List[Card]] = opponents_cards.by_suit
        self.opponents_unplayed_cards: Dict[str, List[Card]] = opponents_unplayed_cards.by_suit

        self.seats_unplayed_cards = {seat: Cards(self.board.hands[seat].unplayed_cards).by_suit for seat in SEATS}
        self.seats_unplayed_cards = {}
        for seat in SEATS:
            self.seats_unplayed_cards[seat] = Cards(self.board.hands[seat].unplayed_cards).by_suit

        # Trumps
        if self.trump_suit:
            self.trump_cards = self.hand_cards.by_suit[self.trump_suit]
            self.opponents_trumps = opponents_unplayed_cards.by_suit[self.trump_suit]
        else:
            self.trump_cards = None
            self.opponents_trumps = None

        # Partners
        if self.is_declarer:
            partners_hand = self.board.hands[self.dummy]
        elif self.is_dummy:
            partners_hand = self.board.hands[self.declarer]
        else:
            partners_hand = None
        if partners_hand:
            self.partners_hand = partners_hand
            partners_cards = Cards(partners_hand.cards)
            self.partners_suit_cards = partners_cards.by_suit
            self.partners_unplayed_cards = Cards(partners_hand.unplayed_cards).by_suit
        else:
            self.partners_suit_cards = {suit: [] for suit in SUITS}
            self.partners_unplayed_cards = {suit: [] for suit in SUITS}

        self.total_unplayed_cards = self._total_unplayed_cards()

        # Declarer and Dummy
        # These card properties must be assigned in this order
        declarers_cards = Cards(board.hands[self.declarer].unplayed_cards)
        self.declarers_suit_cards = declarers_cards.by_suit
        dummys_cards = Cards(board.hands[self.dummy].unplayed_cards)
        self.dummys_suit_cards: Dict[str, List[Card]] = dummys_cards.by_suit
        self.dummys_unplayed_cards: Dict[str, List[Card]] = dummys_cards.by_suit
        self.dummy_suit_strength = self.get_suit_strength(dummys_cards.list)
        self.dummy_suit_tenaces = self._get_tenaces(self.dummys_suit_cards)
        # Short trump hands
        if self.trump_suit:
            declarers_trumps = self.declarers_suit_cards[self.trump_suit]
            dummys_trumps = self.dummys_suit_cards[self.trump_suit]
            if len(declarers_trumps) > len(dummys_trumps):
                self.short_suit_seat = self.dummy
            else:
                self.short_suit_seat = self.declarer

        if self.trump_suit:
            declarers_trumps = self.get_unplayed_cards_by_suit(self.trump_suit, self.declarer)
            dummys_trumps = self.get_unplayed_cards_by_suit(self.trump_suit, self.dummy)
            declarer_longer_trumps = len(declarers_trumps) > len(dummys_trumps)
            if declarer_longer_trumps:
                self.short_hand = self.board.hands[self.dummy]
            else:
                self.short_hand = self.board.hands[self.declarer]

        # Defenders
        if self.is_defender:
            self.dummy_on_left = ((self.seat_index - self.dummy_index) % 4) == 3
            self.dummy_on_right = not self.dummy_on_left
        else:
            self.dummy_on_left = None
            self.dummy_on_right = None

        # Information
        self.trick_number = len(board.tricks)
        self.declarers_target = self.board.contract.target_tricks
        (self.declarers_tricks, self.defenders_tricks) = self._get_trick_count()
        self.suit_rounds = self._get_suit_rounds()

        if not self.is_defender:
            self.dashboard = Dashboard(self)

    @staticmethod
    def cards_by_suit(hand: Hand) -> Dict[str, List[Card]]:
        """Return a dict of unplayed cards by suit for the given hand."""
        cards = Cards(hand.unplayed_cards)
        return cards.by_suit

    @staticmethod
    def get_partners_seat(seat: str) -> str:
        """Return partner's seat."""
        seat_index = SEATS.index(seat)
        partners_index = (seat_index + 2) % 4
        partners_seat = SEATS[partners_index]
        return partners_seat

    def _get_seat(self) -> str:
        """Return the current user's seat."""
        trick = self.board.tricks[-1]
        leader = trick.leader
        leader_index = SEATS.index(leader)
        seat_index = (leader_index + len(trick.cards)) % 4
        seat = SEATS[seat_index]
        return seat

    def cards_for_trick_suit(self, trick: Trick) -> List[Card]:
        """Return a list of cards in the trick suit."""
        return self.hand_cards.by_suit[trick.suit]

    def record_void(self, suit: Suit):
        """Add void to manager voids."""
        manager = global_vars.manager
        manager.voids[self.seat][suit.name] = True

    @staticmethod
    def other_suit_for_signals(suit: Suit) -> str:
        """Return the other suit for signalling."""
        if suit.name == 'S':
            other_suit = 'C'
        elif suit.name == 'C':
            other_suit = 'S'
        elif suit.name == 'H':
            other_suit = 'D'
        elif suit.name == 'D':
            other_suit = 'H'
        return other_suit

    def _get_trump_suit(self) -> Suit:
        """Return the trump suit for the board (if any)."""
        if self.board.contract.is_nt:
            return None
        return self.board.contract.denomination

    @staticmethod
    def get_suit_strength(cards: List[Card]) -> Dict[str, int]:
        """Return a dict of suit high card points keyed on suit name."""
        suit_points = {suit: 0 for suit in SUITS}
        for card in cards:
            suit_points[card.suit.name] += card.high_card_points
        return suit_points

    def get_strongest_suits(self, cards: List[Card]) -> List[Suit]:
        """Return a list of suits that have the highest high card points."""
        suit_points = self.get_suit_strength(cards)
        strong_suits = self.get_list_of_best_scores(suit_points)
        return strong_suits

    def _get_tenaces(self, cards: Dict[str, Card]) -> Dict[str, Card]:
        """Return a dict of suit tenaces keyed on suit name."""
        suit_tenaces = {suit_name: None for suit_name, suit in SUITS.items()}
        for suit, cards in cards.items():
            suit_tenaces[suit] = self.get_suit_tenaces(cards)
        return suit_tenaces

    def get_suit_tenaces(self, cards: List[Card]) -> Card:
        """Return the top card in a tenaces, or None."""
        if not cards:
            return None

        opponents_cards = self.opponents_unplayed_cards[cards[0].suit.name]
        suit = cards[0].suit_name
        for card in cards[:-2]:
            if card.is_honour:
                value = card.value
                missing_card = Card(CARD_VALUES[value-1], suit)
                next_card = Card(CARD_VALUES[value-2], suit)
                if missing_card in opponents_cards and next_card in cards:
                    return next_card
        return None

    def _get_opponents_seats(self) -> Tuple[str, str]:
        """Return a Tuple with right and left hand seats."""
        seat_index = SEATS.index(self.seat)
        left_hand_seat_index = (seat_index + 1) % 4
        right_hand_seat_index = (seat_index + 3) % 4
        return(SEATS[right_hand_seat_index], SEATS[left_hand_seat_index])

    def card_has_been_played(self, card: Card) -> bool:
        """Return True if the card has already been played."""
        for seat in SEATS:
            hand = self.board.hands[seat]
            if card in hand.unplayed_cards:
                return False
        return True

    def get_unplayed_cards_by_suit(self, suit: Suit, seat: str) -> List[Card]:
        """Return a list containing declarers and opponents unplayed cards in a suit."""
        hand = self.board.hands[seat]
        cards = hand.cards_by_suit[suit.name]
        unplayed_cards = [card for card in cards if card in hand.unplayed_cards]
        return unplayed_cards

    def _total_unplayed_cards(self) -> Dict[str, List[Card]]:
        """Return a dict containing all unplayed cards by suit."""
        unplayed_card_list = []
        for seat in SEATS:
            unplayed_card_list += self.hands[seat].unplayed_cards
            unplayed_cards = Cards(unplayed_card_list)
        return unplayed_cards.by_suit

    @staticmethod
    def _sort_cards(cards: List[Card]) -> List[Card]:
        """Return a sorted list of cards."""
        return sorted(cards, reverse=True)

    def long_seat(self, suit: str) -> str:
        my_cards = self.unplayed_cards[suit]
        partners_cards = self.partners_unplayed_cards[suit]
        if len(my_cards) > len(partners_cards):
            return self.seat
        else:
            return self.partner_seat

    def holds_all_winners_in_suit(self, suit: Suit, trick: Trick = None) -> bool:
        """Return True if the partnership holds all the winners in a suit."""
        opponents_unplayed_cards = [card for card in self.opponents_unplayed_cards[suit.name]]
        our_cards = [card for card in self.our_unplayed_cards[suit.name]]
        if trick:
            for card in trick.cards:
                if card.suit == suit:
                    if card in self.opponents_cards[suit.name]:
                        opponents_unplayed_cards.append(card)
                    else:
                        our_cards.append(card)
        opponents_unplayed_cards = Cards(opponents_unplayed_cards).list

        # long_player = self.long_seat(suit.name)
        our_length = len(self.our_unplayed_cards[suit.name])
        opponents_length = len(opponents_unplayed_cards)

        for index, card in enumerate(our_cards):
            if index >= min(opponents_length, our_length):
                return True
            if card.value < opponents_unplayed_cards[0].value:
                return False
        else:
            return False

    def dummy_holds_adjacent_card(self, card: Card) -> bool:
        """Return True if the hand contains the adjacent card."""
        cards = self.dummys_suit_cards[card.suit.name]
        for other_card in cards:
            if other_card.value == card.value + 1 or other_card.value == card.value - 1:
                return True
        return False

    def partnership_long_suits(self, ignore_trumps=True):
        """Return a list of the longest partnership suits."""
        suits = {suit_name: len(self.our_unplayed_cards[suit_name]) for suit_name in SUITS}
        if self.trump_suit:
            if ignore_trumps:
                suits.pop(self.trump_suit.name)
        long_suits = self.get_list_of_best_scores(suits)
        return long_suits

    def can_lead_toward_tenace(self, long_suit: str) -> bool:
        """Return True if we can lead to higher honour in partner's hand."""
        if self.partners_unplayed_cards[long_suit] and self.suit_cards[long_suit]:
            partners_best_card = self.partners_unplayed_cards[long_suit][0]
            my_best_card = self.unplayed_cards[long_suit][0]
            if partners_best_card.is_honour:
                if partners_best_card.value > my_best_card.value + 1:
                    return True
        return False

    @staticmethod
    def get_list_of_best_scores(candidates: Dict[object, int], reverse: bool = False) -> List[object]:
        """Return a list of the best scoring candidates from a dict of candidates."""
        best_candidates = []
        max_score = 0
        min_score = 0
        for key, score in candidates.items():
            if score > max_score:
                max_score = score

        if reverse:
            min_score = max_score
            for key, score in candidates.items():
                if score < min_score:
                    min_score = score

        for key, score in candidates.items():
            if reverse:
                if score == min_score:
                    best_candidates.append(key)
            else:
                if score == max_score:
                    best_candidates.append(key)
        return best_candidates

    def get_winners(self) -> int:
        """Return the current number of winners for declarer."""
        winners = 0
        for suit_name in SUITS:
            for card in self.our_unplayed_cards[suit_name]:
                if self.opponents_unplayed_cards[suit_name]:
                    opponents_top_card_value = self.opponents_unplayed_cards[suit_name][0].value
                    if card.value > opponents_top_card_value:
                        winners += 1
                    else:
                        break
                else:
                    winners += 1
        return winners

    def get_controls(self) -> Dict[str, int]:
        """Return the current number of winners for declarer."""
        controls = {suit_name: 0 for suit_name in SUITS}
        for suit_name in SUITS:
            control_count = 0
            for card in self.our_unplayed_cards[suit_name]:
                if self.opponents_unplayed_cards[suit_name]:
                    opponents_top_card_value = self.opponents_unplayed_cards[suit_name][0].value
                    if card.value > opponents_top_card_value:
                        control_count += 1
                    else:
                        break
                else:
                    control_count += 1
                controls[suit_name] = control_count
        return controls

    def _get_trick_count(self) -> int:
        """Return the number of tricks won by declarer."""
        if self.declarer in 'NS':
            return (self.board.NS_tricks, self.board.EW_tricks)
        else:
            return (self.board.EW_tricks, self.board.NS_tricks)

    def get_entries(self, hand):
        """Return the controlling card in a suit."""
        entries = {suit_name: [] for suit_name in SUITS}
        unplayed_cards = Cards(hand.unplayed_cards)
        suit_cards = unplayed_cards.by_suit
        for suit_name in SUITS:
            cards = suit_cards[suit_name]
            for card in cards:
                if self._is_master(card, entries):
                    entries[suit_name].append(card)
                else:
                    break
        return entries

    def _is_master(self, card: Card, other_masters: Dict[str, List[Card]]) -> bool:
        """Return True if card is a master."""
        # unplayed_cards = [unplayed_card for unplayed_card in self.unplayed_cards[card.suit.name]]
        unplayed_cards = self.total_unplayed_cards[card.suit]
        for master_card in other_masters[card.suit.name]:
            if master_card in unplayed_cards:
                unplayed_cards.remove(master_card)
        for unplayed_card in unplayed_cards:
            if unplayed_card.value > card.value:
                return False
        return True

    def is_winner_declarer(self, card: Card, trick: Trick = None) -> bool:
        """Return True is the card is a winner for declarer."""
        suit = card.suit.name
        opponents_unplayed_cards = [card for card in self.opponents_unplayed_cards[suit]]
        if trick:
            if trick.leader in (self.seat, self.partner_seat):
                if len(trick.cards) > 1:
                    if trick.cards[1].suit.name == suit:
                        opponents_unplayed_cards.append(trick.cards[1])
            else:
                if trick.cards[0].suit.name == suit:
                    opponents_unplayed_cards.append(trick.cards[0])
                if len(trick.cards) > 2:
                    if trick.cards[2].suit.name == suit:
                        opponents_unplayed_cards.append(trick.cards[2])
        # opponents_unplayed_cards = Cards(opponents_unplayed_cards).list
        if not opponents_unplayed_cards:
            return True
        if card.value > sorted(opponents_unplayed_cards, reverse=True)[0].value:
            return True
        return False

    def is_winner_defender(self, trick_card: Card, trick: Trick = None) -> bool:
        """Return True is the card is a winner for defender."""
        card_value = trick_card.value
        if trick:
            if trick.cards[0].value > trick_card.value:
                return False
            if len(trick.cards) == 3:
                value_2 = trick.cards[2].value
                if self.trump_suit:
                    if trick.cards[2].suit == self.trump_suit:
                        value_2 += 13
                    if trick.card.suit == self.trump_suit:
                        card_value += 13
                        card_value = trick_card.value
                if value_2 > card_value:
                    return False
            suit = trick.suit
        else:
            suit = trick_card.suit

        # Get all unplayed cards in the suit
        unplayed_cards = [card for card in self.total_unplayed_cards[suit.name]]

        # Remove dummy's card if it's already played
        if self.dummy_on_right and trick:
            for card in self.dummys_unplayed_cards[suit.name]:
                unplayed_cards.remove(card)

        # Remove my unplayed cards
        for card in self.unplayed_cards[suit.name]:
            unplayed_cards.remove(card)

        if not unplayed_cards:
            return True
        if card_value > unplayed_cards[0].value:
            return True
        return False

    def get_entries_in_other_suits(self, hand: Hand, suit: Suit):
        """Return the entries in a hand other than in the given suit."""
        entries = []
        for suit_name in SUITS:
            if suit_name != suit.name:
                cards = self.get_entries(hand)[suit_name]
                entries.extend(cards)
        return entries

    def missing_honours(self, suit: Suit) -> List[Card]:
        """Return a list of missing honours in the suit."""
        our_cards = self.our_unplayed_cards[suit]
        missing_honours = []
        for index, rank in enumerate('AKQJT'):
            card = Card(rank, suit.name)
            if card in self.total_unplayed_cards[suit]:
                if card not in our_cards:
                    missing_honours.append(card)
        return missing_honours

    def control_suit(self, suit: Suit) -> bool:
        """Return True if player totally controls suit."""
        our_cards = self.our_unplayed_cards[suit.name]
        opponents_cards = self.opponents_unplayed_cards[suit.name]
        if not opponents_cards:
            return True
        index = len(opponents_cards) - 1
        if index > len(our_cards) - 1:
            return False
        if opponents_cards[0].value > our_cards[index].value:
            return True
        return True

    def card_from_my_tenace(self):
        """Return the bottom from a tenace in my hand."""
        dashboard = self.dashboard
        trick = self.board.tricks[-1]
        suit = trick.suit.name
        cards = self.cards_for_trick_suit(trick)
        higher_card = None
        if dashboard.threats[suit]:
            for threat in dashboard.threats[suit]:
                if threat.rank != 'A':
                    for value in range(threat.value+1, 14):
                        card = Card(CARD_VALUES[value], suit)
                        if card in cards:
                            higher_card = card
                            break
                        elif card in self.total_unplayed_cards[suit]:
                            return (None, None)
                    if not higher_card:
                        return (None, None)

                    for value in reversed(range(threat.value)):
                        card = Card(CARD_VALUES[value], suit)
                        if card in cards:
                            return (higher_card, card)
                        if card in self.total_unplayed_cards[suit]:
                            return (None, None)
        return (None, None)

    def card_value(self, card: Card) -> int:
        """Return the card value adjusted for trumps."""
        if self.trump_suit:
            if card.suit == self.trump_suit:
                return card.value + 13
        return card.value

    def touching_honours(self, cards: List[Card]) -> Union[Card, None]:
        """Return the top of touching honours if there is one or None otherwise."""
        for index, card in enumerate(cards[:-1]):
            if card.is_honour and card.value == cards[index+1].value + 1:
                return card
        return None

    def touching_honours_in_hand(self, hand: Hand, suit: str) -> Union[Card, None]:
        """Return the top of touching honours if there is one or None otherwise."""
        cards = Cards(hand.unplayed_cards).by_suit[suit]
        for index, card in enumerate(cards[:-1]):
            if card.is_honour and card.value == cards[index+1].value + 1:
                return card
        return None

    def _longest_suit(self) -> Suit:
        """Return the longest suit in the hand."""
        lengths = {suit: 0 for suit in SUITS}
        for suit in SUITS:
            lengths[suit] = len(self.unplayed_cards[suit])
        long_suits = self.get_list_of_best_scores(lengths)
        if len(long_suits) == 1:
            return Suit(long_suits[0])

        strength = {suit: 0 for suit in long_suits}
        for suit in long_suits:
            strength[suit] = self.get_suit_strength(self.unplayed_cards[suit])
        strong_suits = self.get_list_of_best_scores(lengths)
        if len(strong_suits) == 1:
            return Suit(strong_suits[0])
        return Suit(strong_suits[0])

    def _get_suit_rounds(self) -> Dict[str, int]:
        """Return a dict of rounds played by suit."""
        rounds = {suit: 0 for suit in SUITS}
        for trick in self.board.tricks[:-1]:
            rounds[trick.suit.name] += 1
        return rounds

    def is_tenace(self, card_1: Card, card_2: Card, gap: int = 1) -> bool:
        """Return True if card_1 and card_2 form a tenace."""
        if card_1.suit != card_2.suit:
            return False
        suit = card_1.suit.name
        our_cards = self.our_unplayed_cards[suit]
        if card_1.value > card_2.value:
            top_card = card_1
            bottom_card = card_2
        elif card_1.value < card_2.value:
            top_card = card_2
            bottom_card = card_1
        else:
            return False

        cards = SuitCards(suit).sorted_cards()
        missing_masters = 0
        top_card_check = True
        bottom_card_check = True
        for card in cards:
            if (top_card_check and card != top_card and
                    card not in our_cards and
                    card in self.total_unplayed_cards[suit]):
                return False
            if bottom_card_check and not top_card_check:
                if (card != bottom_card and
                        card not in our_cards and
                        card in self.total_unplayed_cards[suit]):
                    missing_masters += 1
            if card == top_card:
                top_card_check = False
            if card == bottom_card:
                bottom_card_check = False
        if missing_masters == gap:
            return True
        return False
