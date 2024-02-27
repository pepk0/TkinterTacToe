import tkinter as tk

import os
from PIL import Image, ImageTk
from utils.functionality import (
    get_coordinates, place_on_matrix, get_winner, mark_winner, display_text)


class ImageFrame(tk.Frame):
    """A class that contains all the images as attributes used in the game."""

    def __init__(self, img_size: int) -> None:
        super().__init__()
        self.image_one = ImageTk.PhotoImage(
            Image.open(os.path.join("images", "1x1.png")))
        self.image_O = ImageTk.PhotoImage(
            Image.open(os.path.join("images", "o.png")).resize(
                (img_size, img_size)))
        self.image_X = ImageTk.PhotoImage(
            Image.open(os.path.join("images", "x.png")).resize(
                (img_size, img_size)))


class GridPosition(ImageFrame):
    """A class that represents a grid position on the tic-tac-toe field"""

    def __init__(self, number: int, img_size: int) -> None:
        super().__init__(img_size)
        self.number = number

        self.button = tk.Button(self, image=self.image_one, height=110,
                                width=110, background="Gray", border=0,
                                activebackground="Gray")

        self.button.grid(row=0, column=0)

    def on_place(self, parent) -> None:
        """Places either an X or O, image on the pressed
        frame box based on the turn"""
        img = self.image_O if parent.turn % 2 == 0 else self.image_X
        self.button["image"] = img
        parent.turn += 1


class InfoFrame(ImageFrame):
    """A class that gives game information"""

    def __init__(self, img_size: int) -> None:
        super().__init__(img_size)
        self.text_label = tk.Label(
            self, text="Placing: ", font=("Helvetica", 25))
        self.img_label = tk.Label(self, image=self.image_O, height=90)
        self.img_label.grid(row=0, column=1)
        self.text_label.grid(row=0, column=0)

    def set_img(self, parent, element=None, draw=False):
        """sets the appropriate image based on if the 
        game is draw or one of O or X wins"""
        img = self.image_O if parent.turn % 2 == 0 else self.image_X

        if draw:
            img = self.image_one
        elif element:
            img = self.image_O if element == "O" else self.image_X

        self.img_label["image"] = img


class ControlFrame(tk.Frame):
    """A class that stores the buttons that control the game"""

    def __init__(self, parent) -> None:
        super().__init__()
        self.quit_button = tk.Button(
            self, text="Quit Game", bg="#d15e6a", command=self.quit_game)
        self.restart_button = tk.Button(
            self, text="Reset Game", command=self.reset_game)
        self.parent = parent
        self.restart_button.grid(row=0, column=0, padx=20)
        self.quit_button.grid(row=0, column=1)

    def quit_game(self) -> None:
        """quits the game"""
        raise SystemExit

    def reset_game(self) -> None:
        """will destroy the current window"""
        self.parent.destroy()


class MainFrame(tk.Tk):
    """A class that displays all the information
    buttons and grids of the game"""

    def __init__(self) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.turn = 0
        self.matrix_field = [[0] * 3 for _ in range(3)]
        # dict to store matrix coordinates (row, col) to its
        # corresponding grid element
        self.button_mapping = {}
        # starting position of the game frame, adjust for your screen
        self.geometry('+%d+%d' % (700, 200))

        self.info_field = InfoFrame(40)
        self.control_field = ControlFrame(self)

        self.control_field.grid(row=0, column=0, columnspan=3, pady=20)
        self.info_field.grid(row=1, column=0, columnspan=3)

        for number in range(1, 10):
            # places 9 frames making a 3x3 tic-tac-toe pattern
            grid_pos = GridPosition(number, 80)
            row, col = get_coordinates(number)
            self.button_mapping[(row, col)] = grid_pos
            # dynamically calculate position
            # based on the number of the grid position
            grid_pos.grid(row=row + 2, column=col, padx=2, pady=2)
            # on click event binding instead of a button command
            grid_pos.button.bind("<Button-1>",
                                 lambda event, frame=grid_pos:
                                 self.on_button_click(frame))

    def on_button_click(self, frame) -> None:
        """places the correct element on the clicked 
        button and check's if it's a winning move"""
        position = frame.number
        element = "O" if self.turn % 2 == 0 else "X"

        if place_on_matrix(self.matrix_field, element, position):
            # place an appropriate image on the button and info panel
            frame.on_place(self)
            self.info_field.set_img(self)

            # try to find a winner
            winning_pos = get_winner(self.matrix_field, position, element)

            if winning_pos:
                mark_winner(winning_pos, self.button_mapping)
                display_text(self, self.info_field,
                             "The winner is: ", element=element)
                self.matrix_field = [["X"] * 3 for _ in range(3)]
            # a maximum of 9 moves can be made
            # if no one has won by, then it's a draw
            elif self.turn == 9:
                display_text(self, self.info_field,
                             "Game Over! DRAW!", draw=True)
