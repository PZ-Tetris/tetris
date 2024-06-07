import tkinter as tk


class BaseView(tk.Frame):
    """Base view
    """
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.style()
        self.present()

    def style(self):
        """Custom styles definition
        """
        self.configure(background='#D9D9D9')

    def clear(self):
        """Clear page content
        """
        self.pack_forget()
        self.update_idletasks()
