import tkinter as tk

from PIL import Image, ImageTk
from math import ceil
from tkinter import messagebox


class FrameButton(tk.Frame):
    def __init__(self, parent) -> None:
        super().__init__()
        self.image_one = ImageTk.PhotoImage(Image.open(r"imgs\1x1.png"))
        self.image_O = ImageTk.PhotoImage(
            Image.open(r"imgs\o.png").resize((80, 80)))
        self.image_X = ImageTk.PhotoImage(
            Image.open(r"imgs\x.png").resize((80, 80)))

        self.button = tk.Button(self, image=self.image_one, height=110,
                                width=110, background="Gray", border=0,
                                activebackground="Gray")

        def on_press(self) -> None:
            img = self.image_O if parent.turn % 2 == 0 else self.image_X
            self.button.image = img
            self.button["image"] = img
            parent.turn += 1

        self.on_press = on_press
        self.button.grid(row=0, column=0)


class InfoFrame(tk.Frame):
    def __init__(self, parent) -> None:
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

        self.set_img = set_img


class MainFrame(tk.Tk):
    def __init__(self,) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.turn = 0
        self.matrix_field = [[0] * 3 for _ in range(3)]

        self.info_label = InfoFrame(self)

        self.button_one = FrameButton(self)
        self.button_two = FrameButton(self)
        self.button_tree = FrameButton(self)
        self.button_four = FrameButton(self)
        self.button_five = FrameButton(self)
        self.button_six = FrameButton(self)
        self.button_seven = FrameButton(self)
        self.button_eight = FrameButton(self)
        self.button_nine = FrameButton(self)

        self.info_label.grid(row=0, column=0,)
        self.button_one.grid(row=1, column=0, padx=2, pady=2)
        self.button_two.grid(row=1, column=1, padx=2, pady=2)
        self.button_tree.grid(row=1, column=2, padx=2, pady=2)
        self.button_four.grid(row=2, column=0, padx=2, pady=2)
        self.button_five.grid(row=2, column=1, padx=2, pady=2)
        self.button_six.grid(row=2, column=2, padx=2, pady=2)
        self.button_seven.grid(row=3, column=0, padx=2, pady=2)
        self.button_eight.grid(row=3, column=1, padx=2, pady=2)
        self.button_nine.grid(row=3, column=2, padx=2, pady=2)

        def check_for_winner(event, arg: int, button) -> None:
            row, col = ceil(arg / 3) - 1, (arg + 2) % 3
            element = "O" if self.turn % 2 == 0 else "X"

            if self.matrix_field[row][col] != 0:
                return

            self.matrix_field[row][col] = element  # type: ignore
            button.on_press(button)
            self.info_label.set_img(self.info_label, self)

            element = self.matrix_field[row][col]
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

                    if connected == 3:
                        messagebox.showinfo(
                            "Game Finished", f"The winner is: '{element}' !")
                        raise SystemExit

                    elif self.turn == 9:
                        messagebox.showinfo(
                            "Game Finished", f"The game is Draw!")
                        raise SystemExit

                cur_row, cur_col = row, col

        self.button_one.button.bind("<Button-1>", lambda event, arg=1,
                                    button=self.button_one:
                                    check_for_winner(event, arg, button))

        self.button_two.button.bind("<Button-1>", lambda event, arg=2,
                                    button=self.button_two:
                                    check_for_winner(event, arg, button))

        self.button_tree.button.bind("<Button-1>", lambda event, arg=3,
                                     button=self.button_tree:
                                     check_for_winner(event, arg, button))

        self.button_four.button.bind("<Button-1>", lambda event, arg=4,
                                     button=self.button_four:
                                     check_for_winner(event, arg, button))

        self.button_five.button.bind("<Button-1>", lambda event, arg=5,
                                     button=self.button_five:
                                     check_for_winner(event, arg, button))

        self.button_six.button.bind("<Button-1>",
                                    lambda event, arg=6,
                                    button=self.button_six:
                                    check_for_winner(event, arg, button))

        self.button_seven.button.bind("<Button-1>", lambda event, arg=7,
                                      button=self.button_seven:
                                      check_for_winner(event, arg, button))

        self.button_eight.button.bind("<Button-1>", lambda event, arg=8,
                                      button=self.button_eight:
                                      check_for_winner(event, arg, button))

        self.button_nine.button.bind("<Button-1>", lambda event, arg=9,
                                     button=self.button_nine:
                                     check_for_winner(event, arg, button))
