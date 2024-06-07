import sys
import tkinter as tk
from controllers.main_controller import MainController
import helpers.window as helpers
import tkinter.font as tkFont


class App(tk.Tk):
    """App entrypoint
    """
    WINDOW_WIDTH = 550
    WINDOW_HEIGHT = 650

    def __init__(self):
        super().__init__()
        self.style()
        self.position()
        self.present()

    def style(self):
        """Global app styling
        """
        self.title("PZ - Tetris")
        self.iconbitmap(
            './assets/icon.ico' if sys.platform.startswith('win') else '@./assets/icon.xbm')
        self.configure(background='#D9D9D9')

        if "Calibri" in tkFont.families():
            default_font = tkFont.nametofont("TkDefaultFont")
            default_font.configure(family="Calibri", size=16)
            self.option_add("*Font", default_font)

    def position(self):
        """Position the app window at the screen center
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_geometry = helpers.calculate_center_of_screen_position(
            screen_width, screen_height, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.geometry(window_geometry)

        self.resizable(False, False)

    def present(self):
        """Present app content
        """
        main = MainController()
        main.view.pack()


app = App()

if __name__ == "__main__":
    app.mainloop()
