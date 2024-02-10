import tkinter as tk

from PIL import Image, ImageTk
from tkinter import ttk
from math import ceil


class FrameButton(tk.Frame):
    def __init__(self,) -> None:
        super().__init__(width=80, height=80, bg="Gray")
        image_one = ImageTk.PhotoImage(
            Image.open(r"imgs\x.png").resize((80, 80)))
        self.button = tk.Button(self, image=image_one, width=80, height=80,
             command=lambda: on_press(self, image_one))

        self.button.grid(row=0, column=0)

        def on_press(self, image) -> None:
            print("clicked")
            self.button.image = image
            self.button["image"] = image


class MainFrame(tk.Tk):
    def __init__(self,) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.turn = 0
        self.matrix_field = [[0] * 3 for _ in range(3)]

        self.button_one = FrameButton().grid(row=0, column=0, padx=2, pady=2)
        self.button_two = FrameButton().grid(row=0, column=1, padx=2, pady=2)
        self.button_tree = FrameButton().grid(row=0, column=2, padx=2, pady=2)
        self.button_four = FrameButton().grid(row=1, column=0, padx=2, pady=2)
        self.button_five = FrameButton().grid(row=1, column=1, padx=2, pady=2)
        self.button_six = FrameButton().grid(row=1, column=2, padx=2, pady=2)
        self.button_seven = FrameButton().grid(row=2, column=0, padx=2, pady=2)
        self.button_eight = FrameButton().grid(row=2, column=1, padx=2, pady=2)
        self.button_nine = FrameButton().grid(row=2, column=2, padx=2, pady=2)
