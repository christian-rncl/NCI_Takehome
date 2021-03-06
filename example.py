"""NCI take home, example variant implementation
Demonstrates ease of creating aribtrary game variants
Author: Christian Roncal, cjl.roncal@gmail.com
"""

from cardgame import CardGame
from deck import Deck

class ColorGameVariant(CardGame):
    """Example Variant implemenatations
    In this game, there are extra cards with different color points
    Players can also "discard a card".
    Players also have 4 moves each.
    Score calculation also uses a multiplier that doubles a card value\
        if the card number is even.
    """

    def __init__(self):
        # game settings:
        num_players = 3
        color_values = {'red':3, 'yellow':2, 'green':1, 'blue': 4, 'purple': 5}
        deck = Deck(color_values=color_values)
        valid_moves = ['draw', 'disc']

        super(ColorGameVariant, self).__init__(num_players, deck, valid_moves)
        self.num_moves = 6


    def step(self, player, move):
        if move == 'draw':
            card = self._draw()
            player.draw(card)
        else:
            player.get_hand().pop()
            self.num_moves -= 1
        self.num_moves -= 1

    def is_game_over(self):
        return self.num_moves <= 0

    def tally(self, player):
        score = 0

        for card in player.get_hand():
            multiplier = 2 if card.number % 2 == 0 else 1
            score += self._card_deck.get_color_point(card) * card.number * multiplier

        return score

    def pick_winner(self):
        winner = None
        hi_score = 0

        for player in self._players:
            score = self.tally(player)
            if score > hi_score:
                winner = player
                hi_score = score


        return winner, hi_score
