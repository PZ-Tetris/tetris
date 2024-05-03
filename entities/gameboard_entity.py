import tkinter as tk

class Gameboard(tk.Canvas):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height, background='gray75')

        self.width = width
        self.height = height
        self.block_width = 25
        self.game_matrix_width = width // self.block_width
        self.game_matrix_height = height // self.block_width
        self.game_matrix = [[(False, '', False)] * self.game_matrix_width for _ in range(self.game_matrix_height)] # Values: [Is the block filled?, Block color, Is the block active? (currently moving)]
        self.active_block = None