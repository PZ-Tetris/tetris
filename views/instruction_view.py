import tkinter as tk
import tkinterweb

from controls.page_button import PageButton
from views.base_view import BaseView


class InstructionView(BaseView):
    def __init__(self, controller):
        super().__init__(controller)

    def __add_widgets(self):
        back_button = PageButton(
            self, text="Home", command=self.controller.back_to_main)
        frame = tkinterweb.HtmlFrame(self, messages_enabled=False)

        # load a website
        frame.load_website(
            "https://github.com/PZ-Tetris/tetris/blob/master/README.md")
        back_button.grid(column=0, row=0)
        frame.grid(column=0, row=1, columnspan=2)

    def present(self):
        self.__add_widgets()
        self.pack()
