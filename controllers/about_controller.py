from views.about_view import AboutView


class AboutController:
    def __init__(self, previousView):
        self.view = AboutView(self)
        self.previousView = previousView

    def back_to_main(self):
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
