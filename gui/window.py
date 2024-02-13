import tkinter as tk

from PIL import Image, ImageTk
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
        self.image_draw = self.image_O = ImageTk.PhotoImage(
            Image.open(r"imgs\1x1.png").resize((1, 1)))
        self.image_O = ImageTk.PhotoImage(
            Image.open(r"imgs\o.png").resize((40, 40)))
        self.image_X = ImageTk.PhotoImage(
            Image.open(r"imgs\x.png").resize((40, 40)))

        self.text_label = tk.Label(
            self, text="Placing: ", font=("Helvetica", 25))
        self.img_label = tk.Label(self, image=self.image_O, height=90)

        self.img_label.grid(row=0, column=1)
        self.text_label.grid(row=0, column=0)

    def set_img(self, parent, element=None, draw=False):
        img = self.image_O if parent.turn % 2 == 0 else self.image_X

        if draw:
            img = self.image_draw
        elif element:
            img = self.image_O if element == "O" else self.image_X

        self.img_label["image"] = img


class ControlFrame(tk.Frame):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent

        self.quit_button = tk.Button(self, text="Quit Game", bg="#d15e6a")
        self.restart_button = tk.Button(self, text="Reset Game")

        self.restart_button.grid(row=0, column=0, padx=20)
        self.quit_button.grid(row=0, column=1)


class MainFrame(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.turn = 0
        self.matrix_field = [[0] * 3 for _ in range(3)]
        # mapping so we can use it to convert 2d matrix coordinates,
        # to potions in range 1 - 9
        self.button_mapping = {}
        # placement adjust for your screen
        self.geometry('+%d+%d' % (700, 200))

        self.info_field = InfoFrame()
        self.control_field = ControlFrame(self)

        # frame placement
        self.control_field.grid(row=0, column=0, columnspan=3, pady=20)
        self.info_field.grid(row=1, column=0, columnspan=3)

        self.control_field.quit_button.bind(
            "<Button-1>", lambda event: quit_game(event))
        self.control_field.restart_button.bind(
            "<Button-1>", lambda event, parent=self: reset_game(event, parent))

        for i in range(1, 10):
            row, col = get_coordinates(i)
            grid_pos = GridPosition(i)
            self.button_mapping[(row, col)] = grid_pos
            grid_pos.grid(row=row + 2, column=col, padx=2, pady=2,)
            # on click event binding instead of a button command
            grid_pos.button.bind("<Button-1>", lambda event,
                                 frame=grid_pos: on_button_click(event, frame))

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
                    self.info_field.set_img(self, element=element)
                    self.info_field.text_label["text"] = "Winner is: "
                    self.matrix_field = [["X"] * 3 for _ in range(3)]
                # a maximum of 3x3 = 9 moves can be made,
                # if no winner then it's a draw
                elif self.turn == 9:
                    self.info_field.text_label["text"] = "The Game is Draw"
                    self.info_field.set_img(self, draw=True)

        def quit_game(event) -> None:
            raise SystemExit

        def reset_game(event, parent) -> None:
            parent.destroy()
