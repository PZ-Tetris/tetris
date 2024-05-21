from views.game_view import GameView
from controllers.save_score_controller import SaveScoreController


class GameController:
    def __init__(self, previousView):
        self.view = GameView(self)
        self.previousView = previousView

    def save_result(self):
        pass

    # PLACEHOLDER METHOD TO SHOW ALL BLOCKS
    def restart(self):
        self.view.clear()
        self.view = GameView(self)

    def open_save_score(self):
        ctrl = SaveScoreController()
        ctrl.view.present()
        self.view.clear()

    def back_to_main(self):
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
