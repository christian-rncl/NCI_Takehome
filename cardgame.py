"""NCI take home, CardGame, Player base classes
Author: Christian Roncal, cjl.roncal@gmail.com
"""

from abc import ABC, abstractmethod

class Player:
    """ Abstract Base Class for a CardGame player. Child classes\
        must implement tally()

    Args:
        name (str): name kof the player

    Attributes:
        name (str): name of the player
        hand (list of Card): cards in player's hand
    """

    def __init__(self, name: str):
        self.name = name
        self._hand = []
        self._points = 0

    def draw(self, card):
        """Add new card to _hand

        Args:
            card (Card): the card to add to _hand attr
        """
        self._hand.append(card)

    def discard(self, card):
        """Removes card from hand

        Args:
            card (Card): the card to be remove from _hand
        """
        return self._hand.remove(card)

    def get_hand(self):
        """getter for _hand
        """
        return self._hand


class CardGame(ABC):
    """Card game Abstract Base class implements game loop/view

    Args:
        num_players (int): number of players in the game
        card_deck (Deck): deck of cards to use for card game
        valid_moes (list of str): valid user input strings

    Attributes:
        _num_players (int): number of players in the game
        _players (list of Player): players in the game
        _card_deck (Deck): deck of cards to use for card game
        _valid_moes (list of str): valid user input strings
    """

    def __init__(self, num_players, card_deck, valid_moves):
        self._num_players = num_players
        self._players = []
        self._card_deck = card_deck
        self._valid_moves = valid_moves
        self._card_deck.shuffle()

    def start_game(self):
        """ Adds players and Starts a game loop. Stopped by is_game_over.
        Displays prompts and relevant game information.
        """

        def add_players():
            for i in range(self._num_players):
                self._players.append(Player("Player %d" % (i + 1)))

        def parse_move(player_name):
            valid_input = False

            while not valid_input:
                print("%s's turn" % player_name)
                usr_mv = input().lower().strip()
                valid_input = usr_mv in self._valid_moves

                if not valid_input:
                    print("Invalid move. Please try again.")

            return usr_mv

        add_players()
        print("--- Get Ready, Starting Game. ---")

        game_over = False

        while not game_over:
            for player in self._players:
                move = parse_move(player.name)
                self.step(player, move)
                game_over = self.is_game_over()

        self.end_game()

    def _draw(self):
        return self._card_deck.draw()

    @abstractmethod
    def end_game(self):
        """ Finishes game, displays winner or renders etc...
        """
        return NotImplemented

    @abstractmethod
    def step(self, player, move):
        """ Applies move to game environment and user status.
        e.g. draw move makes a player take a card etc...

        Args:
            player (Player): player making the move
            move (str): *validated* move to apply to game and player
        """
        return NotImplemented

    @abstractmethod
    def is_game_over(self) -> bool:
        """ Decides when to terminate game loop
        Returns:
            bool: whether game is over or not
        """
        return NotImplemented

    @abstractmethod
    def tally(self, player):
        """ tallies score of @player

        Args:
            player (Player): player to calculate score for

        Returns:
            score - could be float, int etc....
        """
        return NotImplemented
