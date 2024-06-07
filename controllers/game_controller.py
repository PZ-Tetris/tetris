from helpers.sound_manager import MusicType, SoundManager
from helpers.leaderboard_data_access import LeaderBoardDataAccess
from models.leaderboard_model import LeaderBoardModel
from views.game_view import GameView
from controllers.save_score_controller import SaveScoreController
from tkinter import simpledialog

class GameController:
    """Controller for the game logic
    """
    def __init__(self, previousView, is_random):
        self.view = GameView(self, is_random)
        self.previousView = previousView
        self.is_random = is_random
        self.soun_manager = SoundManager()

    def save_result(self, score):
        """Method for saving game results

        Args:
            score (_type_): the game result
        """
        user_nick = simpledialog.askstring('Save results', "What's your nick?")

        if user_nick is not None:
            with LeaderBoardDataAccess() as data_access:
                data = LeaderBoardModel('', user_nick, score)
                data_access.insert(data)

    # PLACEHOLDER METHOD TO SHOW ALL BLOCKS
    def restart(self):
        """Restart the game progress
        """
        self.view.clear()
        self.view = GameView(self, self.is_random)

    def open_save_score(self, score):
        """Method for navigation to the save score view

        Args:
            score (_type_): the game result
        """
        ctrl = SaveScoreController(self.previousView, score)
        ctrl.view.present()
        self.view.clear()
        self.view.destroy()

    def back_to_main(self):
        """Method for returning to main page
        """
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
        self.soun_manager.play_music(MusicType.MENU)

