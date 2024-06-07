from views.about_view import AboutView


class AboutController:
    """Controller for the about page
    """
    def __init__(self, previousView):
        self.view = AboutView(self)
        self.previousView = previousView

    def back_to_main(self):
        """Go back to the main page
        """
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
