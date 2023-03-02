

class InvalidGameState(Exception):
    """Raised when the game state is invalid."""


class InvalidMove(Exception):
    """Raised when an invalid move is made"""


class InvalidPlayers(Exception):
    """Raised when the players have invalid marks"""

class UnknownGameScore(Exception):
    """Raised when the game has no outcome yet"""
