"""Card game model as described in prompt
Author: Christian Roncal, cjl.roncal@gmail.com
"""

import sys
sys.path.append('model/')
from cardgame import CardGame
from deck import Deck

class ColorCardGame(CardGame):
    """Color card game as descried in prompt.
    2 players take turns drawing cards
    when both players have 3 cards, tally the score and
    declare the winner.
    Score is calculated by color_point * number in the card
    """

    def __init__(self):
        # game settings:
        num_players = 2
        deck = Deck()
        valid_moves = ['draw']

        super(ColorCardGame, self).__init__(num_players, deck, valid_moves)
        self.num_moves = 6

    def step(self, player, move):
        card = self._draw()
        player.draw(card)
        self.num_moves -= 1

    def is_game_over(self):
        return self.num_moves <= 0

    def tally(self, player):
        score = 0

        for card in player.get_hand():
            score += self._card_deck.get_color_point(card) * card.number

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
