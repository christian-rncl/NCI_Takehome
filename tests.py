"""NCI take home, Test suite.
Author: Christian Roncal, cjl.roncal@gmail.com
"""

from itertools import permutations
import pytest
from deck import Deck
from deck_exceptions import EmptyDeckException, InvalidDeckSizeException
from deck import Card

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



#####################
### Assumptions test cases
#####################

def test_assumption_six():
    """test raise exception if deck size is less than the amount\
        of card combinations (assumption #6)
    """
    with pytest.raises(InvalidDeckSizeException):
        Deck(5)
