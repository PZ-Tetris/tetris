import tkinter as tk

from controls.page_button import PageButton
from views.base_view import BaseView


class SaveScoreView(BaseView):
    def __init__(self, controller):
        super().__init__(controller)
        self.unbind_all('<KeyPress>')

    def __add_widgets(self):
        self.text_score = tk.Text(self, height=1, width=10, relief=tk.FLAT, background='#D9D9D9')
        self.text_score.grid(column=0, row=0, columnspan=2, sticky=tk.W+tk.E, pady=(50, 10))
        self.text_score.insert(tk.END, f"Score: {self.controller.score}")
        self.text_score.config(state=tk.DISABLED)
        self.text_nick = tk.Text(self, height=1, width=6, relief=tk.FLAT, background='#D9D9D9')
        self.text_nick.grid(column=0, row=1, pady=(10, 10))
        self.text_nick.insert(tk.END, 'Nick: ')
        self.text_nick.config(state=tk.DISABLED)
        self.text_input = tk.Text(self, height=1, width=22)
        self.text_input.grid(column=1, row=1)
        self.save_button = PageButton(self, text="Save score", command=self.save_score)
        self.save_button.grid(column=0, row=2, columnspan=2, pady=(10, 10))

    def save_score(self):
        nick = self.text_input.get("1.0", "1.16").strip()
        self.controller.set_nick(nick)
        self.controller.save_score()

    def present(self):
        self.__add_widgets()
        self.pack()
        