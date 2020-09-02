"""NCI take home, view for cardgame
Author: Christian Roncal, cjl.roncal@gmail.com
"""

class View:
    """View object containing static methods for
    command line display for card game
    """

    @staticmethod
    def prompt_player(player_name, moves):
        """Displays prompt for @player_name and
        available commands user can enter through @moves
        """
        print("-" * 12)
        print("Make your move %s!" % player_name)
        print("Available Moves:", moves)
        print("-" * 12)

    @staticmethod
    def start_game():
        """Informational display at beginning of game
        """
        print("*** Card Game NCI Take Home ***")
        print("Author: Christian Roncal")
        print("*" * 31)

    @staticmethod
    def display_winner(name, score, hand):
        """ Displays winner, points and winning hand
        usually called at the end of the game
        """
        print("+" * 25)
        print("GAME OVER!")
        print("WINNER: %s with %d points!" % (name, score))
        print("Winning hand:", hand)
        print("+" * 25)

    @staticmethod
    def display_invalid_input():
        """Displayed when user enters invalid input
        """
        print("Invalid move. Please try again")

    @staticmethod
    def display_hand(player_name, hand):
        """Display player's hand. Called after every move
        """
        print("%s's hand: %s " % (player_name, hand))

    @staticmethod
    def display_draw_game():
        print("+" * 25)
        print("GAME OVER!")
        print("DRAW!")
        print("+" * 25)
