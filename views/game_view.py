import tkinter as tk

from controls.page_button import PageButton
from views.base_view import BaseView
from entities.gameboard_entity import Gameboard
from interactors.generate_next_block import BlockGenerator


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

        score_label = tk.Label(self, text="Score: 0")

        self.canvas = Gameboard(self, width=350, height=500)
        self.block_generator = BlockGenerator(self.canvas)

        # PLACEHOLDER NEXT LINE
        self.block_generator.generate_next_block()

        save_button.grid(column=0, row=0, sticky='w', pady=10)
        restart_button.grid(column=1, row=0, pady=10)
        back_button.grid(column=2, row=0, sticky='e', pady=10)

        score_label.grid(column=1, row=1)

        self.canvas.grid(column=0, columnspan=3, row=2, pady=10)

    def present(self):
        self.__add_widgets()
        self.pack()