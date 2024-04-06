import tkinter as tk
from PIL import ImageTk, Image

from controls.page_button import PageButton


class MainView(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.style()
        self.present()

    def __configure_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

    def __add_widgets(self):
        self.im = Image.open("assets/example.jpg")
        new_size = (128, 128 * (float(self.im.height) / self.im.width))
        self.im.thumbnail(new_size, Image.Resampling.LANCZOS)
        self.home_img = ImageTk.PhotoImage(self.im)

        app_name_label = tk.Label(self, text="Tetris", background='#D9D9D9')
        image = tk.Label(self, image=self.home_img)
        play_btn = PageButton(self, text="Play")
        leaderboard_btn = PageButton(
            self, text="Leaderboard", command=self.controller.open_leaderboard)
        about_btn = PageButton(self, text="About")

        app_name_label.grid(column=1, row=1, padx=1, pady=5)
        image.grid(column=1, row=2, padx=1, pady=5)
        play_btn.grid(column=1, row=3, padx=1, pady=5)
        leaderboard_btn.grid(column=1, row=4, padx=1, pady=5)
        about_btn.grid(column=1, row=5, padx=1, pady=5)

    def __show_main_content(self):
        self.__configure_grid()
        self.__add_widgets()

    def style(self):
        self.configure(background='#D9D9D9')

    def clear(self):
        self.destroy()
        self.update_idletasks()

    def present(self, custom_content=None):
        if custom_content is not None:
            self.clear()
            custom_content.pack()
        else:
            self.__show_main_content()
