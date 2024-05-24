from helpers.leaderboard_data_access import LeaderBoardDataAccess
from models.leaderboard_model import LeaderBoardModel
from views.game_view import GameView
from tkinter import simpledialog


class GameController:
    def __init__(self, previousView):
        self.view = GameView(self)
        self.previousView = previousView

    def save_result(self):
        user_nick = simpledialog.askstring('Save results', "What's your nick?")

        if user_nick is not None:
            with LeaderBoardDataAccess() as data_access:
                data = LeaderBoardModel('', user_nick, 0)
                data_access.insert(data)

    # PLACEHOLDER METHOD TO SHOW ALL BLOCKS
    def restart(self):
        self.view.clear()
        self.view = GameView(self)

    def back_to_main(self):
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
