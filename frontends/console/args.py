import argparse

from tic_tac_toe.game.players import Player, RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from .players import ConsolePlayer

PLAYER_CLASSES = {
    "human": ConsolePlayer,
    "random": RandomComputerPlayer
}


def parse_args():
    parser = argparse.ArgumentParser(prog="Tic Tac Toe")
    parser.add_argument("-X", help=f"Pick the player type for the X mark from the following: "
                                   f"{list(PLAYER_CLASSES.keys())}",
                        dest="player_x", choices=PLAYER_CLASSES.keys(), default="human")
    parser.add_argument("-O", help=f"Pick the player type for the O mark from the following: "
                                   f"{list(PLAYER_CLASSES.keys())}",
                        dest="player_o", choices=PLAYER_CLASSES.keys(), default="random")
    parser.add_argument("--starting", help=f"Pick the starting player (X or O)",
                        dest="starting_mark", choices=Mark, type=Mark, default="X")

    args = parser.parse_args()

    player_x = PLAYER_CLASSES[args.player_x](Mark("X"))
    player_o = PLAYER_CLASSES[args.player_o](Mark("O"))

    if args.starting_mark == "O":
        return player_o, player_x, Mark(args.starting_mark)
    else:
        return player_x, player_o, Mark(args.starting_mark)
