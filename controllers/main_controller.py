from controllers.leaderboard_controller import LeaderBoardController
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
