import random
from termcolor import cprint

from .dealer import Dealer as DealerBase, Board
from bridgeobjects import SEATS, BALANCED_SHAPES, SEMI_BALANCED_SHAPES, Call

MODULE_COLOUR = 'green'


SET_HANDS = {
    0: 'Opening ones',
    1: 'Limit bids',
    2: 'Response in new suit',
    3: 'Balanced rebids',
    4: 'Single suited rebids',
    5: 'Two suited rebids',
    6: 'Support for responder',
    # 'Raise responders NT',
    8: 'Response to weak two',
    9: 'Response to 2NT',
    10: 'Response to 2C',
}

class Dealer(DealerBase):
    """Generate deals for Solo stages."""

    def __init__(self, *args, **kwargs):
        super(Dealer, self).__init__(*args, **kwargs)

    def get_set_hand(self, stages, seat):
        """Return a board relevant to set stages."""

        seat_index = SEATS.index(seat)
        # stages = params.set_hands
        stage = int(random.choice(stages))

        # Solo hands
        if stage == 0:  #  Opening ones
            board = self.deal_opening_one_board(seat_index)
        elif stage == 1:  #  Limit bids
            board = self.deal_limit_bids_responder_board(seat_index)
        elif stage == 2:  #  Response in new suit
            board = self.deal_respond_in_new_suit_board(seat_index)
        elif stage == 3:  #  Balanced rebids
            board = self.deal_balanced_rebid_board(seat_index)
        elif stage == 4:  #  Single suited rebids
            board = self.deal_single_suited_rebid_board(seat_index)
        elif stage == 5:  #  Two suited rebids
            board = self.deal_two_suited_rebid_board(seat_index)
        elif stage == 6:  #  Support for responder
            board = self.deal_support_for_responder_board(seat_index)
        elif stage == 7:  #  Raise responders NT
            board = self.deal_raise_responder_nt_board(seat_index)
        elif stage == 8:  #  Response to weak two
            board = self.deal_response_to_weak_two_board(seat_index)
        elif stage == 9:  #  Response to 2NT
            board = self.deal_response_to_two_nt_board(seat_index)
        elif stage == 10:  #  Response to 2C
            board = self.deal_response_to_two_clubs_board(seat_index)
        else:
            board = self.deal_random_board()
        board.stage = stage
        return board

    def deal_opening_one_board(self, seat_index):
        """Return a board suitable for an opening one."""
        found = False
        loop = 0
        board = None
        while not found:
            loop += 1
            openers_hand = self.engine.get_hand_from_points_and_shape([12, 22])
            hands = {seat_index: openers_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[seat_index])
            board.dealer = SEATS[seat_index]
            auction = self._generate_auction_calls(board)
            if auction[0].level == 1 and self._valid_overcalls(auction):
                found = True
        return board

    def deal_limit_bids_responder_board(self, seat_index):
        """Return a board suitable for limited responses to opener."""
        found = False
        loop = 0
        board = None
        while not found:
            loop += 1
            openers_hand = self.deal_opening_one_hand()
            if (openers_hand.shape in BALANCED_SHAPES and
                    openers_hand.high_card_points <= 14):
                responders_hand = self._deal_limit_bids_responder_nt(openers_hand)
            else:
                responders_hand = self._deal_limit_bids_responder_support(openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {partners_index: openers_hand, seat_index: responders_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[partners_index])
            board.dealer = SEATS[partners_index]
            auction = self._generate_auction_calls(board)
            if self._valid_overcalls(auction):
                found = True
        return board

    def _deal_limit_bids_responder_nt(self, openers_hand):
        """Return a hand suitable for an NT response after opening one."""
        shapes = BALANCED_SHAPES.extend(SEMI_BALANCED_SHAPES)
        responders_hand = self.engine.get_hand_from_points_and_shape([0, 17], shapes, openers_hand)
        return responders_hand

    def _deal_limit_bids_responder_support(self, openers_hand):
        """Return a hand suitable for an NT response after opening one."""
        board = Board()
        board.hands[0] = openers_hand
        board.players[0].hand = openers_hand
        openers_bid = board.players[0].make_bid(board)
        loop = 1
        found = False
        responders_hand = None
        get_hand = self.engine.get_hand_from_points_and_shape
        while not found:
            loop += 1
            responders_hand = get_hand([3, 16], None, openers_hand)
            if (openers_bid.is_minor and
                    responders_hand.four_card_major_or_better and
                    responders_hand.hcp >= 6):
                found = False
            elif (openers_bid.is_suit_call and
                    responders_hand.suit_holding[openers_bid.denomination] < 4):
                found = False
            else:
                found = True
        return responders_hand

    def deal_balanced_rebid_board(self, seat_index):
        """Return a board suitable for balanced response."""
        get_hand = self.engine.get_hand_from_points_and_shape
        found = False
        loop = 0
        board = None
        while not found:
            loop += 1
            openers_hand = get_hand([15, 19], BALANCED_SHAPES)
            responders_hand = get_hand([3, 20], None, openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {seat_index: openers_hand, partners_index: responders_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[seat_index])
            board.dealer = SEATS[seat_index]
            auction = self._generate_auction_calls(board)
            if len(auction) >= 5:
                openers_bid = auction[0]
                responders_bid = auction[2]
                if (openers_bid.denomination != responders_bid.denomination and
                        not responders_bid.is_no_trumps):
                    if self._valid_overcalls(auction):
                        found = True
        return board

    def deal_single_suited_rebid_board(self, seat_index):
        """Return a board suitable for single suit response."""
        get_hand = self.engine.get_hand_from_points_and_shape
        found = False
        loop = 0
        board = None
        while not found:
            loop += 1
            openers_hand = get_hand([12, 19], self.SINGLE_SUITED_SHAPES)
            responders_hand = get_hand([6, 15], None, openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {seat_index: openers_hand, partners_index: responders_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[seat_index])
            board.dealer = SEATS[seat_index]
            auction = self._generate_auction_calls(board)
            if len(auction) >= 5:
                openers_bid_one = auction[0]
                responders_bid = auction[2]
                openers_bid_two = auction[4]
                if (openers_bid_one.denomination == openers_bid_two.denomination and
                        responders_bid.denomination != openers_bid_one.denomination and
                        responders_bid.denomination != openers_bid_two.denomination):
                    if self._valid_overcalls(auction):
                        found = True
        return board

    def deal_two_suited_rebid_board(self, seat_index):
        """Return a board suitable for two suit response."""
        get_hand = self.engine.get_hand_from_points_and_shape
        found = False
        board = None
        while not found:
            openers_hand = get_hand([12, 19], self.TWO_SUITED_SHAPES)
            responders_hand = get_hand([6, 15], None, openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {seat_index: openers_hand, partners_index: responders_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[seat_index])
            board.dealer = SEATS[seat_index]
            auction = self._generate_auction_calls(board)
            openers_bid_one = auction[0]
            if len(auction) >= 5:
                openers_bid_two = auction[4]
            else:
                # dummy inserted to ensure a 2 level bid
                openers_bid_two = Call('2C')
            responders_bid = auction[2]
            if len(auction) <= 3:
                found = False
            elif not self._valid_overcalls(auction):
                found = False
            elif responders_bid.is_pass:
                found = False
            elif openers_bid_two.is_pass:
                found = False
            elif openers_bid_one.denomination == openers_bid_two.denomination:
                found = False
            elif responders_bid.is_game:
                found = False
            elif len(openers_hand.cards) != 13:
                found = False
            elif len(responders_hand.cards) != 13:
                found = False
            elif responders_bid.is_suit_call:
                if openers_bid_two.denomination != responders_bid.denomination:
                    found = True
                else:
                    found = False
            else:
                found = True
        return board

    def deal_support_for_responder_board(self, seat_index):
        """Return a board suitable for supporting responder's suit."""
        get_hand = self.engine.get_hand_from_points_and_shape
        openers_hand = get_hand([12, 19], self.TWO_SUITED_SHAPES)
        loop = 1
        found = False
        board = None
        get_hand = self.engine.get_hand_from_points_and_shape
        while not found:
            loop += 1
            responders_hand = get_hand([6, 16], None, openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {seat_index: openers_hand, partners_index: responders_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[seat_index])
            board.dealer = SEATS[seat_index]
            auction = self._generate_auction_calls(board)
            openers_bid = auction[0]
            responders_bid = auction[2]
            if responders_bid.is_suit_call:
                if self._valid_overcalls(auction):
                    responders_suit = responders_bid.denomination
                    if (openers_bid.denomination != responders_suit and
                            openers_hand.suit_holding[responders_suit] >= 4):
                        found = True
        return board

    def deal_respond_in_new_suit_board(self, seat_index):
        """Return a board where responder bids new suit."""
        get_hand = self.engine.get_hand_from_points_and_shape
        openers_hand = get_hand([12, 19], self.TWO_SUITED_SHAPES)
        loop = 1
        found = False
        board = None
        get_hand = self.engine.get_hand_from_points_and_shape
        while not found:
            loop += 1
            responders_hand = get_hand([6, 16], None, openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {partners_index: openers_hand, seat_index: responders_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[partners_index])
            board.dealer = SEATS[partners_index]
            auction = self._generate_auction_calls(board)
            openers_bid = auction[0]
            responders_bid = auction[2]
            if responders_bid.is_suit_call:
                if self._valid_overcalls(auction):
                    responders_suit = responders_bid.denomination
                    if openers_bid.denomination != responders_suit:
                        found = True
        return board

    def deal_raise_responder_nt_board(self, seat_index):
        """Return a hand where opener raises responder nt."""
        get_hand = self.engine.get_hand_from_points_and_shape
        loop = 1
        found = False
        board = None
        while not found:
            loop += 1
            openers_hand = get_hand([12, 19], SEMI_BALANCED_SHAPES)
            responders_hand = get_hand([6, 16], BALANCED_SHAPES, openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {seat_index: openers_hand, partners_index: responders_hand}
            board = self.engine.create_board_from_hands(hands)
            board.dealer = SEATS[seat_index]
            auction = self._generate_auction_calls(board)
            if len(auction) >= 5:
                openers_bid = auction[0]
                responders_bid = auction[2]
                openers_rebid = auction[4]
                if (openers_bid.is_suit_call and
                        responders_bid.is_no_trumps and
                        openers_rebid.is_no_trumps):
                    if self._valid_overcalls(auction):
                        found = True
        return board

    def deal_response_to_weak_two_board(self, seat_index):
        """Return a board requiring a response to weak two opening."""
        get_hand = self.engine.get_hand_from_points_and_shape
        found = False
        loop = 0
        board = None
        while not found:
            loop += 1
            openers_hand = get_hand([6, 10], self.WEAK_TWO_SHAPES)
            responders_hand = get_hand([12, 19], None, openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {partners_index: openers_hand, seat_index: responders_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[partners_index])
            board.dealer = SEATS[partners_index]
            auction = self._generate_auction_calls(board)
            openers_bid = auction[0]
            if openers_bid.level == 2:
                if self._valid_overcalls(auction):
                    found = True
        return board

    def deal_response_to_two_nt_board(self, seat_index):
        """Return a board requiring a response to two NT opening."""
        get_hand = self.engine.get_hand_from_points_and_shape
        found = False
        loop = 0
        board = None
        while not found:
            loop += 1
            openers_hand = get_hand([20, 22], BALANCED_SHAPES)
            responders_hand = get_hand([0, 12], None, openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {partners_index: openers_hand, seat_index: responders_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[partners_index])
            board.dealer = SEATS[partners_index]
            auction = self._generate_auction_calls(board)
            if self._valid_overcalls(auction):
                found = True
        return board

    def deal_response_to_two_clubs_board(self, seat_index):
        """Return a board requiring a response to two clubs opening."""
        get_hand = self.engine.get_hand_from_points_and_shape
        found = False
        loop = 0
        board = None
        while not found:
            loop += 1
            openers_hand = get_hand([23, 30])
            responders_hand = get_hand([0, 12], None, openers_hand)
            partners_index = (seat_index + 2) % 4
            hands = {partners_index: openers_hand, seat_index: responders_hand}
            board = self.engine.create_board_from_hands(hands, SEATS[partners_index])
            board.dealer = SEATS[partners_index]
            auction = self._generate_auction_calls(board)
            if self._valid_overcalls(auction):
                found = True
        return board