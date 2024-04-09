import tkinter as tk

from controls.page_button import PageButton
from views.base_view import BaseView


class GameView(BaseView):
    def __init__(self, controller):
        super().__init__(controller)

    def __add_widgets(self):
        self.columnconfigure([0, 1, 2], minsize=165)

        save_button = PageButton(
            self, text="Save result", command=self.controller.save_result)
        restart_button = PageButton(
            self, text="Restart", command=self.controller.restart)
        back_button = PageButton(
            self, text="Home", command=self.controller.back_to_main)

        score_label = tk.Label(self, text="Actual score: 0")

        canvas = tk.Canvas(self, width=350, height=500, background='gray75')

        save_button.grid(column=0, row=0, sticky='w', pady=10)
        restart_button.grid(column=1, row=0, pady=10)
        back_button.grid(column=2, row=0, sticky='e', pady=10)

        score_label.grid(column=1, row=1)

        canvas.grid(column=0, columnspan=3, row=2, pady=10)

    def present(self):
        self.__add_widgets()
        self.pack()
