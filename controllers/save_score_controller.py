from views.save_score_view import SaveScoreView


class SaveScoreController:
    def __init__(self):
        self.view = SaveScoreView(self)
        self.main_view = None

    def back_to_main(self):
        self.main_view.present()
        self.view.clear()
        self.view.destroy()
