from views.game_view import GameView


class GameController:
    def __init__(self, previousView):
        self.view = GameView(self)
        self.previousView = previousView

    def save_result(self):
        pass

    def restart(self):
        pass

    def back_to_main(self):
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
