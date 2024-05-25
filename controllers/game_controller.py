from helpers.sound_manager import MusicType, SoundManager
from helpers.leaderboard_data_access import LeaderBoardDataAccess
from models.leaderboard_model import LeaderBoardModel
from views.game_view import GameView
from controllers.save_score_controller import SaveScoreController
from tkinter import simpledialog

class GameController:
    def __init__(self, previousView, is_random):
        self.view = GameView(self, is_random)
        self.previousView = previousView
        self.is_random = is_random
        self.soun_manager = SoundManager()

    def save_result(self, score):
        user_nick = simpledialog.askstring('Save results', "What's your nick?")

        if user_nick is not None:
            with LeaderBoardDataAccess() as data_access:
                data = LeaderBoardModel('', user_nick, score)
                data_access.insert(data)

    # PLACEHOLDER METHOD TO SHOW ALL BLOCKS
    def restart(self):
        self.view.clear()
        self.view = GameView(self, self.is_random)

    def open_save_score(self, score):
        ctrl = SaveScoreController(self.previousView, score)
        ctrl.view.present()
        self.view.clear()
        self.view.destroy()

    def back_to_main(self):
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
        self.soun_manager.play_music(MusicType.MENU)

