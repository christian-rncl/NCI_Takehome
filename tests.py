"""NCI take home, Test suite.
Author: Christian Roncal, cjl.roncal@gmail.com
"""

from itertools import permutations, combinations
import pytest
import sys
sys.path.append('model/')
sys.path.append('.')
from classic_game import ColorCardGame
from deck import Deck
from deck_exceptions import EmptyDeckException, InvalidDeckSizeException
from deck import Card
from cardgame import Player

#####################
### Prompt test cases
#####################

def test_draw_basic():
    """ Tests draw() function as defined in take home prompt #2
    """
    deck = Deck() # default unshuffled deck
    expected = ['(green : 10)', '(green : 9)', '(green : 8)', '(green : 7)',\
                '(green : 6)', '(green : 5)', '(green : 4)', '(green : 3)',\
                '(green : 2)', '(green : 1)', '(yellow : 10)', '(yellow : 9)',\
                '(yellow : 8)', '(yellow : 7)', '(yellow : 6)', '(yellow : 5)',\
                '(yellow : 4)', '(yellow : 3)', '(yellow : 2)', '(yellow : 1)',\
                '(red : 10)', '(red : 9)', '(red : 8)', '(red : 7)', '(red : 6)',\
                '(red : 5)', '(red : 4)', '(red : 3)', '(red : 2)', '(red : 1)']
    actual = []

    for _ in range(len(expected)):
        actual.append(str(deck.draw()))

    assert actual == expected

    with pytest.raises(EmptyDeckException):
        deck.draw()


def test_draw_stress():
    """ Tests draw() function as defined in take home prompt #2 with many cards
    """
    max_cards = 1000000
    deck = Deck(max_cards) # default unshuffled deck

    for _ in range(max_cards):
        deck.draw()

    with pytest.raises(EmptyDeckException):
        deck.draw()

def test_shuffle():
    """ Tests shuffle() function as defined in take home prompt #1 with many cards
    """
    deck = Deck()
    before = deck.card_deck.copy()
    times_diff = 0

    for _ in range(3000):
        deck.shuffle()
        times_diff = times_diff + 1 if before != deck.card_deck else times_diff

    assert times_diff/500 > .9999

def test_sort_cards():
    """ Tests sort as defined in #3 in take home prompt. Tests all possible permutations
    """

    deck = Deck(color_values={'red':3, 'yellow':2, 'green':1, 'blue':4, 'purple':5, 'orange': 6})

    def check_sort(card_deck, key):
        seen_colors = []
        last_number_seen = 0

        for card in card_deck:
            if card.color not in seen_colors:
                seen_colors.append(card.color)

            assert last_number_seen < card.number

        assert seen_colors == list(key)

    for color_order in permutations(deck._color_values.keys()):
        deck.sort_cards(color_order)
        check_sort(deck.card_deck, color_order)


def test_sort_cards_stress():
    """ Tests sort as defined in #3 in take home prompt.\
        Tests all possible permutations, with many cards
    """

    n_cards = 5000
    deck = Deck(color_values={'red':3, 'yellow':2, 'green':1, 'blue':4,\
                'purple':5, 'orange': 6}, deck_sz=n_cards)

    def check_sort(card_deck, key):
        seen_colors = []
        last_number_seen = 0

        for card in card_deck:
            if card.color not in seen_colors:
                seen_colors.append(card.color)

            assert last_number_seen < card.number

        assert seen_colors == list(key)

    for color_order in permutations(deck._color_values.keys()):
        deck.sort_cards(color_order)
        check_sort(deck.card_deck, color_order)

def test_card_equality():
    """ Tests equality __eq__ of cards and if they can be removed\
        in lists with list.remove()
    """
    blue_2_card = Card('blue', 2)
    other_blue_2 = Card('blue', 2)
    red_3_card = Card('red', 3)

    assert blue_2_card == blue_2_card # should be true because same instanec
    assert blue_2_card == other_blue_2 # different instance
    assert blue_2_card != red_3_card

    lst = [blue_2_card, other_blue_2, red_3_card]
    lst.remove(blue_2_card)
    assert lst == [other_blue_2, red_3_card]
    lst.remove(other_blue_2)
    assert lst == [red_3_card]
    lst.remove(red_3_card)
    assert lst == []

#####################
### CardGame tests
#####################

def test_cardgame_basic():
    """Basic unit test of color card game
    """
    cardgame = ColorCardGame()
    cardgame.add_players()
    players = cardgame._players
    assert len(players) == 2
    p1, p2 = players[0], players[1]

    assert cardgame.num_moves == 6
    assert not cardgame.is_game_over()
    for _ in range(3):
        cardgame.step(p1, "draw")
        cardgame.step(p2, "draw")
    assert cardgame.is_game_over

    p1_score = cardgame.tally(p1)
    p2_score = cardgame.tally(p2)

    winner, score = cardgame.pick_winner()

    if winner.name == p1.name:
        assert score == p1_score
        assert p1_score > p2_score
    else:
        assert score == p2_score
        assert p2_score > p1_score

def test_validation():
    """Testing validation for parsing user inputs
    """
    cardgame = ColorCardGame()
    assert cardgame.validate_move("draw")
    assert cardgame.validate_move("DRAW")
    assert cardgame.validate_move("dRaW")
    assert cardgame.validate_move("    dRaW    ")
    assert not cardgame.validate_move("")
    assert not cardgame.validate_move("random")
    assert not cardgame.validate_move("        ")

def test_score_calculation():
    """Test score calculation for classic game
    """
    deck = Deck() # default unshuffled deck
    possible_hands = combinations(deck.card_deck, 3)
    cardgame = ColorCardGame()
    color_values = {'red':3, 'yellow':2, 'green':1}

    def tally_hand(hand):
        total = 0
        for card in hand:
            total += color_values[card.color] * card.number
        return total

    player = Player("Joe")
    for hand in possible_hands:
        player._hand = hand
        assert cardgame.tally(player) == tally_hand(hand)




#####################
### Assumptions test cases
#####################

def test_assumption_six():
    """test raise exception if deck size is less than the amount\
        of card combinations (assumption #6)
    """
    with pytest.raises(InvalidDeckSizeException):
        Deck(5)
