from dataclasses import dataclass
from typing import TypeAlias, Callable

from tic_tac_toe.game.players import Player
from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import Mark, GameState, Grid
from tic_tac_toe.logic.validators import validate_players

ErrorHandler: TypeAlias = Callable[[Exception], None]


@dataclass(frozen=True)
class TicTacToe:
    player_one: Player
    player_two: Player
    renderer: Renderer
    error_handler: ErrorHandler | None = None

    def __post_init__(self):
        validate_players(self.player_one, self.player_two)

    def play(self, starting_mark: Mark = Mark("X")) -> None:
        game_state = GameState(Grid(), starting_mark)
        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                break
            player = self.get_current_player(game_state)
            try:
                game_state = player.make_move(game_state)
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)

    def get_current_player(self, game_state: GameState) -> Player:
        if game_state.current_mark is self.player_one.mark:
            return self.player_one
        else:
            return self.player_two
