import tkinter as tk
import tkinter.ttk as ttk
from typing import List
from PIL import ImageTk, Image

from controls.page_button import PageButton
from models.leaderboard_model import LeaderBoardModel
from views.base_view import BaseView

columns = ('Nick', 'Score')


class LeaderBoardView(BaseView):
    def __init__(self, controller):
        super().__init__(controller)

    def __configure_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
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

        sort_asc_button = PageButton(
            self, text="ASC", image=self.up_arrow_img, command=self.controller.sort_score_data_asc)
        sort_nick_asc_button = PageButton(
            self, text="ASC-NICK", image=self.up_arrow_img, command=self.controller.sort_nick_data_asc, background="#694948")
        home_button = PageButton(
            self, text="Home", image=self.home_img, command=self.controller.back_to_main)
        sort_desc_button = PageButton(
            self, text="DESC", image=self.down_arrow_img, command=self.controller.sort_score_data_desc)
        sort_nick_button = PageButton(
            self, text="DESC-NICK", image=self.down_arrow_img, command=self.controller.sort_nick_data_desc, background="#694948")
        sort_asc_button.grid(column=0, row=0, padx=10, pady=10)
        sort_nick_asc_button.grid(column=1, row=0, padx=10, pady=10)
        home_button.grid(column=2, row=0, padx=10, pady=10)
        sort_nick_button.grid(column=3, row=0, padx=10, pady=10)
        sort_desc_button.grid(column=4, row=0, padx=10, pady=10)

        self.__add_tab()

    def __add_tab(self, ordering_mode='DESC', col='score'):
        self.tab = ttk.Treeview(self, columns=columns, show='headings')
        self.tab.heading('Nick', text='Nick')
        self.tab.heading('Score', text='Score')
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
