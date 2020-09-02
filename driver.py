"""NCI take home
main driver for take hom asses.
Contains implementation of game as described in prompt
Author: Christian Roncal, cjl.roncal@gmail.com
"""

from classic_game import ColorCardGame
# from example import ColorGameVariant
from controller import Controller
from view import View


if __name__ == '__main__':
    cardgame = ColorCardGame()
    # cardgame = ColorGameVariant()
    view = View()
    controller = Controller(cardgame, view)
    controller.start()
