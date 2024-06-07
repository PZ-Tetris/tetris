import tkinter as tk

from controls.page_button import PageButton
from views.base_view import BaseView


class AboutView(BaseView):
    """About view
    """
    def __init__(self, controller):
        super().__init__(controller)

    def __add_widgets(self):
        """Add page widgets
        """
        about_info = tk.LabelFrame(self, text="About", background='#D9D9D9')
        authors = tk.LabelFrame(about_info, text="Authors", background='#D9D9D9')
        technologies = tk.LabelFrame(
            about_info, text="Technologies", background='#D9D9D9')
        authors_txt = tk.Label(
            authors, text=f"Adrian Sławiński\nKrzysztof Żelazny\nMaciej Dąbrowski\nPiotr Kowalczyk\nPiotr Ptak\nSzymon Antkowiak", background='#D9D9D9')
        technologies_txt = tk.Label(
            technologies, text=f"tkinter\nPillow\nPyMuPDF", background='#D9D9D9')
        back_button = PageButton(
            self, text="Home", command=self.controller.back_to_main)
        back_button.grid(column=0, row=0)
        about_info.grid(column=0, row=1)
        authors.pack(padx=5, pady=5)
        authors_txt.pack(padx=5, pady=5)
        technologies.pack(padx=5, pady=5)
        technologies_txt.pack(padx=5, pady=5)

    def present(self):
        """Add show page content
        """
        self.__add_widgets()
        self.pack()
