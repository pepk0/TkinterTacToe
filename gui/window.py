import tkinter as tk

from PIL import Image, ImageTk
from tkinter import ttk
from math import ceil


class FrameButton(tk.Frame):
    def __init__(self, matrix: list, position: int, main) -> None:
        super().__init__()
        self.image_one = ImageTk.PhotoImage(Image.open(r"imgs\1x1.png"))
        self.image_O = ImageTk.PhotoImage(
            Image.open(r"imgs\o.png").resize((80, 80)))
        self.image_X = ImageTk.PhotoImage(
            Image.open(r"imgs\x.png").resize((80, 80)))

        self.button = tk.Button(self, image=self.image_one,
                                height=110, width=110,
                                background="Gray", border=0,
                                activebackground="Gray",
                                command=lambda: on_press(self))

        self.button.grid(row=0, column=0)

        def on_press(self) -> None:
            row = ceil(position / 3) - 1
            col = (position + 2) % 3

            if matrix[row][col] == 0:
                element = "O" if main.turn % 2 == 0 else "X"
                img = self.image_O if main.turn % 2 == 0 else self.image_X

                matrix[row][col] = element
                self.button.image = img
                self.button["image"] = img
                main.turn += 1


class MainFrame(tk.Tk):
    def __init__(self,) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.turn = 0
        self.matrix_field = [[0] * 3 for _ in range(3)]

        self.button_one = FrameButton(self.matrix_field, 1, self).grid(
            row=0, column=0, padx=2, pady=2)
        self.button_two = FrameButton(self.matrix_field, 2, self).grid(
            row=0, column=1, padx=2, pady=2)
        self.button_tree = FrameButton(self.matrix_field, 3, self).grid(
            row=0, column=2, padx=2, pady=2)
        self.button_four = FrameButton(self.matrix_field, 4, self).grid(
            row=1, column=0, padx=2, pady=2)
        self.button_five = FrameButton(self.matrix_field, 5, self).grid(
            row=1, column=1, padx=2, pady=2)
        self.button_six = FrameButton(self.matrix_field, 6, self).grid(
            row=1, column=2, padx=2, pady=2)
        self.button_seven = FrameButton(self.matrix_field, 7, self).grid(
            row=2, column=0, padx=2, pady=2)
        self.button_eight = FrameButton(self.matrix_field, 8, self).grid(
            row=2, column=1, padx=2, pady=2)
        self.button_nine = FrameButton(self.matrix_field, 9, self).grid(
            row=2, column=2, padx=2, pady=2)

