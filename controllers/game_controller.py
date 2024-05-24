from helpers.sound_manager import MusicType, SoundManager
from views.game_view import GameView
from controllers.save_score_controller import SaveScoreController


class GameController:
    def __init__(self, previousView, is_random):
        self.view = GameView(self, is_random)
        self.previousView = previousView
        self.is_random = is_random
        self.soun_manager = SoundManager()

    def save_result(self):
        pass

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

