from views.instruction_view import InstructionView


class InstructionController:
    """Controller for instruction page
    """
    def __init__(self, previousView):
        self.view = InstructionView(self)
        self.previousView = previousView

    def back_to_main(self):
        """Method for returning to main page
        """
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
