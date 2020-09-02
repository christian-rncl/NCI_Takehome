"""NCI take home, controller for cardgame
follows MVC pattern.
Author: Christian Roncal, cjl.roncal@gmail.com
"""

class Controller:
    """MVC controller for card game take home

    Args:
        cardgame (CardGame): Model. Contains cardgame logic
        view (View): View. Contains static methods for\
            printing game status
    """

    def __init__(self, cardgame, view):
        self.cardgame = cardgame
        self.view = view

    def parse_move(self, player_name):
        """User input validationn loop. Makes sure
        player enters a valid move. Otherwise prompts user again.
        """

        valid_input = False

        while not valid_input:
            self.view.display_player_prompt(player_name, self.cardgame.get_valid_moves())
            usr_mv = input().lower().strip()
            valid_input = self.cardgame.validate_move(usr_mv)

            if not valid_input:
                self.view.display_invalid_input()

        return usr_mv

    def start(self):
        """ Adds players and Starts a game loop. Stopped by is_game_over.
        Displays prompts and relevant game information.
        """

        self.view.display_game_start()
        self.cardgame.add_players()

        game_over = False

        while not game_over:
            for player in self.cardgame.get_players():
                move = self.parse_move(player.name)
                self.cardgame.step(player, move)
                self.view.display_hand(player.name, player.get_hand())
                game_over = self.cardgame.is_game_over()

        winner, score = self.cardgame.pick_winner()

        if not winner:
            self.view.display_draw_game()
        else:
            self.view.display_winner(winner.name, score, winner.get_hand())
