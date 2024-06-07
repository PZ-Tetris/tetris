from controllers.game_controller import GameController
from views.game_mode_view import GameModeView


class GameModeController:
    """Controller for the game mode logic
    """
    def __init__(self, previousView):
        self.view = GameModeView(self)
        self.previousView = previousView

    def back_to_main(self):
        """Method for returning to main page
        """
        self.previousView.present()
        self.view.clear()
        self.view.destroy()

    def open_standard_game(self):
        """On click handler for displaying game view & starting standard game
        """
        ctrl = GameController(self.view, False)
        ctrl.view.present()
        self.view.clear()

    def open_random_speed_game(self):
        """On click handler for displaying game view & starting random speed game
        """
        ctrl = GameController(self.view, True)
        ctrl.view.present()
        self.view.clear()