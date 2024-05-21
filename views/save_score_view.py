import tkinter as tk
import tkinterweb

from controls.page_button import PageButton
from views.base_view import BaseView


class SaveScoreView(BaseView):
    def __init__(self, controller):
        super().__init__(controller)
        self.unbind_all('<KeyPress>')

    def __add_widgets(self):
        self.text_input = tk.Text(self, height=1, width=25)
        self.text_input.grid(column=0, row=0)

    def present(self):
        self.__add_widgets()
        self.pack()
        