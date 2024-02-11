import tkinter as tk

from PIL import Image, ImageTk
from tkinter import ttk
from math import ceil
from tkinter import messagebox


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
            row, col = ceil(position / 3) - 1, (position + 2) % 3

            if matrix[row][col] == 0:
                element = "O" if main.turn % 2 == 0 else "X"
                img = self.image_O if main.turn % 2 == 0 else self.image_X

                matrix[row][col] = element
                self.button.image = img
                self.button["image"] = img
                main.turn += 1


class InfoFrame(tk.Frame):
    def __init__(self,) -> None:
        super().__init__()
        pass


class MainFrame(tk.Tk):
    def __init__(self,) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.turn = 0
        self.matrix_field = [[0] * 3 for _ in range(3)]

        self.button_one = FrameButton(self.matrix_field, 1, self)
        self.button_two = FrameButton(self.matrix_field, 2, self)
        self.button_tree = FrameButton(self.matrix_field, 3, self)
        self.button_four = FrameButton(self.matrix_field, 4, self)
        self.button_five = FrameButton(self.matrix_field, 5, self)
        self.button_six = FrameButton(self.matrix_field, 6, self)
        self.button_seven = FrameButton(self.matrix_field, 7, self)
        self.button_eight = FrameButton(self.matrix_field, 8, self)
        self.button_nine = FrameButton(self.matrix_field, 9, self)

        self.button_one.grid(row=0, column=0, padx=2, pady=2)
        self.button_two.grid(row=0, column=1, padx=2, pady=2)
        self.button_tree.grid(row=0, column=2, padx=2, pady=2)
        self.button_four.grid(row=1, column=0, padx=2, pady=2)
        self.button_five.grid(row=1, column=1, padx=2, pady=2)
        self.button_six.grid(row=1, column=2, padx=2, pady=2)
        self.button_seven.grid(row=2, column=0, padx=2, pady=2)
        self.button_eight.grid(row=2, column=1, padx=2, pady=2)
        self.button_nine.grid(row=2, column=2, padx=2, pady=2)

        def check_for_winner(event, arg: int) -> None:
            row, col = ceil(arg / 3) - 1, (arg + 2) % 3
            
            if self.matrix_field[row][col] != 0:
                return
            
            element = "O" if self.turn % 2 == 0 else "X"
            self.matrix_field[row][col] = element  # type: ignore

            directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
            cur_row, cur_col = row, col

            while directions:

                next_row, next_col = directions.pop()
                connected = 1

                for i in range((3 * 2) - 2):

                    if i == 3 - 1:
                        cur_row, cur_col = row, col
                        next_row, next_col = next_row * -1, next_col * -1

                    cur_row, cur_col = next_row + cur_row, next_col + cur_col

                    if 0 <= cur_row < 3 and 0 <= cur_col < 3:
                        if self.matrix_field[cur_row][cur_col] == element:
                            connected += 1

                    if connected >= 3:
                        self.matrix_field[row][col] = 0
                        messagebox.showinfo(
                            "Game Finished", f"Won => {element}")
                        raise SystemExit

                cur_row, cur_col = row, col

            self.matrix_field[row][col] = 0

        self.button_one.button.bind(
            "<Button-1>", lambda event, arg=1: check_for_winner(event, arg))
        self.button_two.button.bind(
            "<Button-1>", lambda event, arg=2: check_for_winner(event, arg))
        self.button_tree.button.bind(
            "<Button-1>", lambda event, arg=3: check_for_winner(event, arg))
        self.button_four.button.bind(
            "<Button-1>", lambda event, arg=4: check_for_winner(event, arg))
        self.button_five.button.bind(
            "<Button-1>", lambda event, arg=5: check_for_winner(event, arg))
        self.button_six.button.bind(
            "<Button-1>", lambda event, arg=6: check_for_winner(event, arg))
        self.button_seven.button.bind(
            "<Button-1>", lambda event, arg=7: check_for_winner(event, arg))
        self.button_eight.button.bind(
            "<Button-1>", lambda event, arg=8: check_for_winner(event, arg))
        self.button_nine.button.bind(
            "<Button-1>", lambda event, arg=9: check_for_winner(event, arg))

