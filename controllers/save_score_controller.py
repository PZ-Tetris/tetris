from helpers.leaderboard_data_access import LeaderBoardDataAccess
from views.save_score_view import SaveScoreView
from models.leaderboard_model import LeaderBoardModel


class SaveScoreController:
    def __init__(self, main_view, score):
        self.nick = None
        self.score = score
        self.view = SaveScoreView(self)
        self.main = main_view

    def back_to_main(self):
        self.main.present()
        self.view.clear()
        self.view.destroy()

    def set_nick(self, nick: str):
        self.nick = nick

    def save_score(self):
        with LeaderBoardDataAccess() as data_access:
            data = LeaderBoardModel(0, self.nick, self.score)
            data_access.insert(data)
        self.back_to_main()
