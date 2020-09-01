from cardgame import CardGame, Player
from deck import Deck

class ColorGame_Variant(CardGame):

    def __init__(self):
        # game settings:
        num_players = 2
        color_values = {'red':3, 'yellow':2, 'green':1, 'blue': 4, 'purple': 5}
        deck = Deck(color_values=color_values)
        valid_moves = ['draw', 'disc']

        super(ColorGame_Variant, self).__init__(num_players, deck, valid_moves)
        self.num_moves = 7

    def step(self, player, move):
        if move == 'draw':
            card = self._draw()
            player.draw(card)
        else:
            player.get_hand().pop()
            self.num_moves -= 1

        self.num_moves -= 1
        print("%s's hand: %s" % (player.name, player.get_hand()))

    def is_game_over(self):
        return self.num_moves <= 0

    def tally(self, player):
        score = 0

        for card in player.get_hand():
            multiplier = 2 if card.number % 2 == 0 else 1
            score += self._card_deck.get_color_point(card) * card.number * multiplier

        return score

    def end_game(self):
        winner = None
        hi_score = 0

        for player in self._players:
            score = self.tally(player)
            if score > hi_score:
                winner = player
                hi_score = score

        print("Game Over!")
        print("The winner is: %s with %d points!" % (winner.name, hi_score))
        print("Winning hand: %s" % (winner.get_hand()))

game = ColorGame_Variant()
game.start_game()