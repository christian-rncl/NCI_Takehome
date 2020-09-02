"""NCI take home, exceptions for deck objects
Author: Christian Roncal, cjl.roncal@gmail.com
"""

class InvalidDeckSizeException(Exception):
    """ Thrown when the deck size is smaller than the number of possible card combinations

    Args:
        msg (str): Human readable error message

    Attributes:
        msg (str): Human readable error message
    """

    def __init__(self, msg="Deck size < number of possible card combinations"):
        super(InvalidDeckSizeException, self).__init__(msg)

class EmptyDeckException(Exception):
    """ Thrown when a user/dev tries to draw from an empty deck

    Args:
        msg (str): Human readable error message

    Attributes:
        msg (str): Human readable error message
    """

    def __init__(self, msg="Deck is empty."):
        super(EmptyDeckException, self).__init__(msg)
