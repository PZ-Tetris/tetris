import io
import tkinter as tk
import fitz
import os
from pathlib import Path
from controls.page_button import PageButton
from views.base_view import BaseView
from PIL import Image, ImageTk


class InstructionView(BaseView):
    def __init__(self, controller):
        super().__init__(controller)

    def retrieve_file_absolute_path(self, file_name = "doc.pdf"):
        if os.path.exists(file_name):
            path = f'{Path().absolute()}/{file_name}'

            return path
        else:
            raise FileNotFoundError()

    def show_pdf(self, path, page_number, canvas):
        self.retrieve_file_absolute_path(path)
        self.pdf_document = fitz.open(path)
        self.page = self.pdf_document.load_page(page_number)
        pix = self.page.get_pixmap()
        img_data = pix.tobytes("ppm")
        self.img = Image.open(io.BytesIO(img_data))
        self.photo = ImageTk.PhotoImage(image=self.img)
        canvas.create_image(0, 0, image=self.photo, anchor='nw')

    def __add_widgets(self):
        back_button = PageButton(
            self, text="Home", command=self.controller.back_to_main)
        canvas = tk.Canvas(self, width=550, height=600)
        self.show_pdf('./assets/instruction.pdf', 0, canvas)
        back_button.grid(column=0, row=0)
        canvas.grid(column=0, row=1)

    def present(self):
        self.__add_widgets()
        self.pack()
