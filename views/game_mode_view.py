import tkinter as tk
from controls.page_button import PageButton
from views.base_view import BaseView

class GameModeView(BaseView):
    """Game mode view
    """
    def __init__(self, controller):
        super().__init__(controller)

    def __configure_grid(self):
        """Configure page grid
        """
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

    def __add_widgets(self):
        """Add widgets
        """
        standard_btn = PageButton(
            self, text="Standard", command=self.controller.open_standard_game)
        random_speed_btn = PageButton(
            self, text="Random speed", command=self.controller.open_random_speed_game)
        back_btn = PageButton(
            self, text="Home", command=self.controller.back_to_main)

        standard_btn.grid(column=1, row=1, padx=1, pady=(50, 5), sticky="n")
        random_speed_btn.grid(column=1, row=2, padx=1, pady=5, sticky="n")
        back_btn.grid(column=1, row=3, padx=1, pady=(5, 50), sticky="n")

    def present(self):
        """Show page content
        """
        self.__configure_grid()
        self.__add_widgets()
        self.pack(fill=tk.BOTH, expand=True)