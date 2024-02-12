import tkinter as tk

from PIL import Image, ImageTk
from tkinter import messagebox
from utils.functionality import (
    get_coordinates, place_on_matrix, get_winner, mark_winner)


class GridPosition(tk.Frame):
    def __init__(self, number: int) -> None:
        super().__init__()
        self.image_one = ImageTk.PhotoImage(Image.open(r"imgs\1x1.png"))
        self.image_O = ImageTk.PhotoImage(
            Image.open(r"imgs\o.png").resize((80, 80)))
        self.image_X = ImageTk.PhotoImage(
            Image.open(r"imgs\x.png").resize((80, 80)))
        self.number = number

        self.button = tk.Button(self, image=self.image_one, height=110,
                                width=110, background="Gray", border=0,
                                activebackground="Gray")

        self.button.grid(row=0, column=0)

    def on_place(self, parent) -> None:
        img = self.image_O if parent.turn % 2 == 0 else self.image_X
        self.button["image"] = img
        parent.turn += 1


class InfoFrame(tk.Frame):
    def __init__(self) -> None:
        super().__init__()
        self.image_O = ImageTk.PhotoImage(
            Image.open(r"imgs\o.png").resize((40, 40)))
        self.image_X = ImageTk.PhotoImage(
            Image.open(r"imgs\x.png").resize((40, 40)))

        self.label = tk.Label(text="is placing", font=("Helvetica", 25))
        self.img_label = tk.Label(image=self.image_O, height=90)

        self.img_label.grid(row=0, column=0, columnspan=1)
        self.label.grid(row=0, column=1, columnspan=2, sticky="w")

    def set_img(self, parent):
        img = self.image_O if parent.turn % 2 == 0 else self.image_X
        self.img_label["image"] = img


class MainFrame(tk.Tk):
    def __init__(self,) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.turn = 0
        self.matrix_field = [[0] * 3 for _ in range(3)]
        # mapping so we can use it to convert 2d matrix coordinates,
        # to potions in range 1 - 9
        self.button_mapping = {}

        self.info_field = InfoFrame()

        # frame placement
        for i in range(1, 10):
            row, col = get_coordinates(i)
            grid_pos = GridPosition(i)
            self.button_mapping[(row, col)] = grid_pos
            grid_pos.grid(row=row + 1, column=col, padx=2, pady=2,)
            # on click event binding instead of a button command
            grid_pos.button.bind("<Button-1>", lambda event,
                                 frame=grid_pos: on_button_click(event, frame))

        self.info_field.grid(row=0, column=0)

        def on_button_click(event, frame) -> None:
            position = frame.number
            element = "O" if self.turn % 2 == 0 else "X"

            if place_on_matrix(self.matrix_field, element, position):
                # place an appropriate image on the button and info panel
                frame.on_place(self)
                self.info_field.set_img(self)

                winning_pos = get_winner(self.matrix_field, position, element)

                if winning_pos:
                    mark_winner(winning_pos, self.button_mapping)
                    messagebox.showinfo(
                        "Game Finished", f"The winner is: '{element}' !")
                    raise SystemExit

            # a maximum of 3x3 = 9 moves can be made,
            # if no winner then it's a draw
            if self.turn == 9:
                messagebox.showinfo(
                    "Game Finished", f"The game is Draw!")
                raise SystemExit
