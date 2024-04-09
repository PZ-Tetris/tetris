import tkinter as tk


class BaseView(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.style()
        self.present()

    def style(self):
        self.configure(background='#D9D9D9')

    def clear(self):
        self.pack_forget()
        self.update_idletasks()
