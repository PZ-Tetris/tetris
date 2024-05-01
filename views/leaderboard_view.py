import tkinter as tk
import tkinter.ttk as ttk
from typing import List
from PIL import ImageTk, Image
from functools import partial

from controls.page_button import PageButton
from models.leaderboard_model import LeaderBoardModel
from views.base_view import BaseView

columns = ('nick', 'score')


class LeaderBoardView(BaseView):
    def __init__(self, controller):
        super().__init__(controller)

    def __configure_grid(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=5)

    def __add_widgets(self):
        self.up_arrow_img = ImageTk.PhotoImage(
            Image.open("assets/up_arrow.png"))
        self.down_arrow_img = ImageTk.PhotoImage(
            Image.open("assets/down_arrow.png"))
        self.home_img = ImageTk.PhotoImage(
            Image.open("assets/home.png"))

        home_button = PageButton(
            self, text="Home", image=self.home_img, command=self.controller.back_to_main)
        home_button.grid(column=2, row=0, padx=10, pady=10)

        self.__add_tab()

    def __add_tab(self, ordering_mode='DESC', col='score'):
        print(ordering_mode)
        arrow_down = ' ⇓'
        arrow_up = ' ⇑'
        arrow = arrow_down if ordering_mode == 'ASC' else arrow_up

        self.tab = ttk.Treeview(self, columns=columns, show='headings')

        for name in columns:
            is_selected = name.lower() == col
            command = partial(self.controller.sort_data,
                              'ASC' if is_selected and ordering_mode == 'DESC' else 'DESC',
                              name)
            self.tab.heading(column=name,
                             text=name.capitalize() + arrow * int(is_selected),
                             command=command)

        data: List[LeaderBoardModel] = self.controller.get_data(
            ordering_mode, col)

        for entry in data:
            self.tab.insert('', tk.END, values=str(entry))
        self.tab.grid(column=0, row=1, columnspan=5,
                      padx=10, pady=10, sticky="ew")

    def __clear_tab(self):
        self.tab.destroy()

    def recreate_tab(self, ordering_mode, col='score'):
        self.__clear_tab()
        self.__add_tab(ordering_mode, col)

    def present(self):
        self.__configure_grid()
        self.__add_widgets()
        self.pack()
