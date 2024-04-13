import tkinter as tk

class Gameboard(tk.Canvas):
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height, background='gray75')

        self.width = width
        self.height = height