import re

from tic_tac_toe.game.players import Player
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Move


class ConsolePlayer(Player):
    def get_move(self, game_state: GameState) -> Move | None:
        while not game_state.game_over:
            try:
                index = grid_to_index(input(f"{self.mark}'s move: ").strip())
            except ValueError:
                print("Coordinates should be in the form of A1 or 1A")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print(f"Cell is already occupied, pick an empty cell.")
        return None


def grid_to_index(coordinate: str) -> int:
    """Based on the given coordinate of form 'A1', '1A', ... '3C', 'C3', returns the index in a 9 position string"""
    number = re.findall(r'[123]', coordinate)
    if len(number) != 1:
        raise ValueError("Coordinate should contain a single number, either 1, 2 or 3.")
    letter = re.findall(r'[ABC]', coordinate.upper())
    if len(letter) != 1:
        raise ValueError("Coordinate should contain a single letter, either A, B or C.")
    return ((int(number[0]) - 1) * 3) + ['A', 'B', 'C'].index(letter[0])
