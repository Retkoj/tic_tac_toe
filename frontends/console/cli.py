from tic_tac_toe.game.engine import TicTacToe

from .args import parse_args
from .renderers import ConsoleRenderer


def main() -> None:
    player_one, player_two, starting_mark = parse_args()
    TicTacToe(player_one, player_two, ConsoleRenderer()).play(starting_mark)
