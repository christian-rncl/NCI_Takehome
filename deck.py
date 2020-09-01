"""NCI take home, Deck of cards implementation
Author: Christian Roncal, cjl.roncal@gmail.com
"""

import random
from itertools import product
from deck_exceptions import InvalidDeckSizeException, EmptyDeckException

class Card:
    """Basic card class nothing much to say.

    Args:
        color (str): representing color
        color_point (int): corresponding color point of card
        number (int): number value of card

    """
    def __init__(self, color: str, number: int):
        self.color = color
        self.number = number

    def __repr__(self):
        return "(%s : %d)" % (self.color, self.number)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self.color == other.color and self.number == other.number


class Deck:
    """Deck of cards implementation.

    Args:
        max_num (int): The maximum number v
        color_values (dict of (str, int)): Available colors for cards,\
                        and their corresponding 'color point'
        deck_sz (int): number of cards, if None, it will be max_num*number of card\
                        colors (all possib combinations.)

    Attributes:
        _color_values (dict of str:int): Available colors for cards, and their\
                        corresponding 'color point'
        card_deck (list of Card): object references built from color_values and\
                        max_num. Has length max_num* number of card colors\
                        (all possib. combinations)
    """

    def __init__(self,
                 deck_sz=None,
                 max_num=10,
                 color_values=None):

        def create_card_deck(color_values):
            """ Creates a card deck based on color_values, max_num and num cards

            Returns:
                A list of Card object references containing deck_sz or max_num*number of card colors

            Raises:
                InvalidDeckSizeException: deck_sz is not None and < max_num*|card colors|
            """

            if color_values is None:
                color_values = {'red':3, 'yellow':2, 'green':1}
            self._color_values = color_values

            # create a generator for all (color, number_val) combinations
            card_combinations = product(color_values.keys(), range(1, max_num+1))
            all_cards = [Card(comb[0], comb[1]) for comb in card_combinations]

            if deck_sz and deck_sz < len(all_cards):
                # exception based on assumption #6
                raise InvalidDeckSizeException()

            if not deck_sz:
                return all_cards # Deck must contain one of each possible card

            # this is where flyweight pattern is used. Additional cards in the deck beyond\
            # the original instances are just references
            num_extra_cards = deck_sz - len(all_cards)
            return all_cards + random.choices(all_cards, k=num_extra_cards)


        self.card_deck = create_card_deck(color_values)

    def draw(self):
        """"Take card from top of deck by calling pop() on list of cards (index -1),\
            removing last element from card_deck

        Returns:
            last element of the card_deck attribute

        Raises:
            EmptyDeckException:
        """
        if len(self.card_deck) <= 0:
            # based on project specification #2
            raise EmptyDeckException()

        return self.card_deck.pop()

    def shuffle(self):
        """ Shuffles card_deck by calling shuffle()
        """
        random.shuffle(self.card_deck)

    def get_color_point(self, card):
        """ returns color point of card based on color_values attribute.

        Args:
            card (Card): card object to get points of.

        Returns:
            color points (int) of card
        """
        return self._color_values[card.color]

    def sort_cards(self, color_key_list):
        """Sorts on the @color_key_list arg as described in prompt #4. eg
        [(red: 1), (green, 5), (red,0), (yellow, 3), (green, 2)], [yellow, green, red]
        -> [(yellow,3), (green,2), (green,5), (red,0), (red,1)]

        Time complexity: O(n + nlogn): O(n) to group elements, O(nlogn) for sorting
        Space complexity: O(n): for the dictionary

        Args:
            color_key_list: list of Colors
        """

        print('----')
        color_groups = {color:[] for color in self._color_values.keys()}

        # group cards by color in a dictionary O(n) time, O(n) space
        for card in self.card_deck:
            color_groups[card.color].append(card)

        # sort each color group by number O(knlog(n)) where k is the number of colors
        for group in color_groups.values():
            group.sort(key=lambda card: card.number)

        ans = []
        # concatenate sorted lists in color_groups in the order given by\
        # @color_key_list roughly O(n)*
        for color_key in  color_key_list:
            ans += color_groups[color_key]

        self.card_deck = ans
