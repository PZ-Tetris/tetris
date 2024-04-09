from controllers.leaderboard_controller import LeaderBoardController
from controllers.game_controller import GameController
from controllers.about_controller import AboutController
from views.main_view import MainView


class MainController:
    def __init__(self):
        self.view = MainView(self)
        self.model = None

    def open_leaderboard(self):
        """On click handler for displaying leaderboard view
        """
        ctrl = LeaderBoardController(self.view)
        ctrl.view.present()
        self.view.clear()

    def open_game(self):
        """On click handler for displaying game view
        """
        ctrl = GameController(self.view)
        ctrl.view.present()
        self.view.clear()

    def open_about(self):
        """On click handler for displaying game view
        """
        ctrl = AboutController(self.view)
        ctrl.view.present()
        self.view.clear()
