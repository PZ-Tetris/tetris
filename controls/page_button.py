import tkinter as tk


class PageButton(tk.Button):
    def __init__(self, parent, text, command=None, image=None):
        super().__init__(parent)
        self.configure(background="#484969",
                       foreground='#FFFFFF', width=15 if image is None else 64, text=text, image=image, command=command)
