import tkinter as tk

from helpers.sound_manager import SoundManager


class PageButton(tk.Button):
    """Custom button with basic app styling applied

    Args:
        tk (_type_): _description_
    """

    def __init__(self, parent, text, command=None, image=None, background="#484969"):
        super().__init__(parent)
        self.configure(background=background,
                       foreground='#FFFFFF', width=15 if image is None else 64, text=text, image=image, command=command)
        self.sound_manager = SoundManager()
        
        self.bind("<Enter>", self.on_hover)
        self.bind("<Button-1>", self.on_click)
        self.command_callback = command

    def on_hover(self, event):
        self.sound_manager.play_hover_sound()

    def on_click(self, event):
        self.sound_manager.play_click_sound()
        self.command_callback()
