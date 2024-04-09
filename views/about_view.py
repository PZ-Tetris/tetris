import tkinter as tk

from controls.page_button import PageButton
from views.base_view import BaseView


class AboutView(BaseView):
    def __init__(self, controller):
        super().__init__(controller)

    def __add_widgets(self):

        back_button = PageButton(
            self, text="Home", command=self.controller.back_to_main)
        back_button.grid(column=0, row=0)

    def present(self):
        self.__add_widgets()
        self.pack()
