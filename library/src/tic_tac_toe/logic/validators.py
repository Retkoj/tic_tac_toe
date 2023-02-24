from __future__ import annotations

from typing import TYPE_CHECKING

from tic_tac_toe.logic.exceptions import InvalidGameState, InvalidPlayers

if TYPE_CHECKING:
    from tic_tac_toe.game.players import Player
    from tic_tac_toe.logic.models import Grid, GameState, Mark

import re


def validate_grid(grid: Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Grid must consist of 9 cells, containing either a 'X', 'O' or space. "
                         "For example: 'XO  OXO X'")


def validate_number_of_marks(grid: Grid) -> None:
    """Validate that both marks occur as often, or one mark occurs at most 1 time more than the other mark"""
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Number of X's and O's are not congruent")


def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    """Validate that the starting_mark occurs as often or more often than the other mark"""
    if ((grid.x_count > grid.o_count and starting_mark != "X") or
            (grid.o_count > grid.x_count and starting_mark != "O")):
        raise InvalidGameState(f"Wrong number of X's and O's given starting mark '{starting_mark}'")


def validate_winner(grid: Grid, starting_mark: Mark, winner: Mark | None) -> None:
    if winner == "X":
        if starting_mark == 'X':
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Wrong number of X's and O's: invalid winning state.")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Wrong number of X's and O's: invalid winning state.")
    elif winner == "O":
        if starting_mark == "O":
            if grid.o_count <= grid.x_count:
                raise InvalidGameState("Wrong number of X's and O's: invalid winning state.")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Wrong number of X's and O's: invalid winning state.")


def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(game_state.grid, game_state.starting_mark, game_state.winner)


def validate_players(player_one: Player, player_two: Player) -> None:
    if player_one.mark is player_two.mark:
        raise InvalidPlayers
