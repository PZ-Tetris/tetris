import tkinter as tk
import tkinter.ttk as ttk
from typing import List
from PIL import ImageTk, Image
from functools import partial
from enum import StrEnum, Enum, auto

from controls.page_button import PageButton
from models.leaderboard_model import LeaderBoardModel
from views.base_view import BaseView


class Column(StrEnum):
    NICK = auto()
    SCORE = auto()


class Ordering(Enum):
    ASC = False
    DESC = True


class LeaderBoardView(BaseView):
    """Leaderboard view
    """
    def __init__(self, controller):
        super().__init__(controller)

    def __configure_grid(self):
        """Configure grid settings
        """
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=5)

    def __add_widgets(self):
        """Add widgets to the page
        """
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

    def __add_tab(self, ordering: Ordering = Ordering.DESC, ord_col: Column = Column.SCORE):
        """Add tab

        Args:
            ordering (Ordering, optional): column ordering. Defaults to Ordering.DESC.
            ord_col (Column, optional): currently ordered column. Defaults to Column.SCORE.
        """
        arrow_down = ' ⇓'
        arrow_up = ' ⇑'
        arrow = arrow_down if ordering.value else arrow_up

        self.tab = ttk.Treeview(self, columns=list(Column), show='headings')

        for column in Column:
            is_selected = column is ord_col
            command = partial(self.controller.sort_data,
                              Ordering(not ordering.value or not is_selected),
                              column)
            self.tab.heading(column=column,
                             text=column.capitalize() + arrow * int(is_selected),
                             command=command)

        data: List[LeaderBoardModel] = self.controller.get_data(
            ordering, ord_col)

        for entry in data:
            self.tab.insert('', tk.END, values=(entry.nick, entry.score))
        self.tab.grid(column=0, row=1, columnspan=5,
                      padx=10, pady=10, sticky="ew")

    def __clear_tab(self):
        """Clear tab content
        """
        self.tab.destroy()

    def recreate_tab(self, ordering: Ordering, ord_col: Column):
        """Recrate tab with new content
        """
        self.__clear_tab()
        self.__add_tab(ordering, ord_col)

    def present(self):
        """Present page details
        """
        self.__configure_grid()
        self.__add_widgets()
        self.pack()
