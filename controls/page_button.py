import tkinter as tk


class PageButton(tk.Button):
    """Custom button with basic app styling applied

    Args:
        tk (_type_): _description_
    """

    def __init__(self, parent, text, command=None, image=None, background="#484969"):
        super().__init__(parent)
        self.configure(background=background,
                       foreground='#FFFFFF', width=15 if image is None else 64, text=text, image=image, command=command)
