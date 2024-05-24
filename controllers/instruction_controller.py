from views.instruction_view import InstructionView


class InstructionController:
    def __init__(self, previousView):
        self.view = InstructionView(self)
        self.previousView = previousView

    def back_to_main(self):
        self.previousView.present()
        self.view.clear()
        self.view.destroy()
