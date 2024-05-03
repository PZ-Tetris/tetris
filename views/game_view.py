import tkinter as tk
import os

from controls.page_button import PageButton
from views.base_view import BaseView
from entities.gameboard_entity import Gameboard
from interactors.generate_next_block import BlockGenerator
from interactors.move_block_interactor import MoveBlockInteractor
from interactors.rotate_block_interactor import RotateBlockInteractor
from interactors.drop_block_interactor import DropBlockInteractor

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
        self.move_block_interactor = MoveBlockInteractor(self.canvas)
        self.rotate_block_interactor = RotateBlockInteractor(self.canvas)
        self.drop_block_interactor = DropBlockInteractor(self.canvas)

        self.bind_all('<Down>', self.move_block_interactor.move_block_down)
        self.bind_all('<Right>', self.move_block_interactor.move_block_right)
        self.bind_all('<Left>', self.move_block_interactor.move_block_left)
        self.bind_all('<Up>', self.rotate_block_interactor.rotate_block)
        self.bind_all('<space>', self.drop_block_interactor.drop_block)

        save_button.grid(column=0, row=0, sticky='w', pady=10)
        restart_button.grid(column=1, row=0, pady=10)
        back_button.grid(column=2, row=0, sticky='e', pady=10)

        score_label.grid(column=1, row=1)

        self.canvas.grid(column=0, columnspan=3, row=2, pady=10)

    def update(self):
        # Check if all blocks are inactive
        all_inactive = all(self.canvas.game_matrix[i][j][2] == 'na'
                        for i in range(self.canvas.game_matrix_height)
                        for j in range(self.canvas.game_matrix_width))

        # If all blocks are inactive, generate the next block
        if all_inactive:
            self.block_generator.generate_next_block()

        # Schedule the next call of this function in 1/30 second
        self.after(1000 // 30, self.update)

        # DEBUG: Print the game matrix to the console
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(20):
            print(self.canvas.game_matrix[i])

        self.canvas.delete("all")  # Remove everything from canvas
        for i in range(self.canvas.game_matrix_height):
            for j in range(self.canvas.game_matrix_width):
                value, block_type, status = self.canvas.game_matrix[i][j]
                if value != 0:  # If the block exists
                    x1 = j * self.canvas.block_width
                    y1 = i * self.canvas.block_width
                    x2 = x1 + self.canvas.block_width
                    y2 = y1 + self.canvas.block_width
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=block_type)  # Draw the block

    def present(self):
        self.__add_widgets()
        self.update()
        self.pack()
