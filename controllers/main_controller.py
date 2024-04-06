from controllers.leaderboard_controller import LeaderBoardController
from views.main_view import MainView


class MainController:
    def __init__(self):
        self.view = MainView(self)
        self.model = None

    def open_leaderboard(self):
        ctrl = LeaderBoardController()
        self.view.present(custom_content=ctrl.view)
