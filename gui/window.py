import tkinter as tk
from tkinter import ttk
from math import ceil


class MainFrame(tk.Tk):
    def __init__(self, ) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.turn = 0
        self.matrix_field = [[0] * 3 for _ in range(3)]

        self.position_one = tk.Button(
            self, text="", width=12, height=5, bg="Grey", relief="flat",
            command=lambda: place_spot(self, 1, self.position_one))

        self.position_two = tk.Button(
            self, text="", width=12, height=5, bg="Grey", relief="flat",
            command=lambda: place_spot(self, 2, self.position_two))

        self.position_three = tk.Button(
            self, text="", width=12, height=5, bg="Gray", relief="flat",
            command=lambda: place_spot(self, 3, self.position_three))

        self.position_four = tk.Button(
            self, text="", width=12, height=5, bg="Grey", relief="flat",
            command=lambda: place_spot(self, 4, self.position_four))

        self.position_five = tk.Button(
            self, text="", width=12, height=5, bg="Grey", relief="flat",
            command=lambda: place_spot(self, 5, self.position_five))

        self.position_six = tk.Button(
            self, text="", width=12, height=5, bg="Grey", relief="flat",
            command=lambda: place_spot(self, 6, self.position_six))

        self.position_seven = tk.Button(
            self, text="", width=12, height=5, bg="Grey", relief="flat",
            command=lambda: place_spot(self, 7, self.position_seven))

        self.position_eight = tk.Button(
            self, text="", width=12, height=5, bg="Grey", relief="flat",
            command=lambda: place_spot(self, 8, self.position_eight))

        self.position_nine = tk.Button(
            self, text="", width=12, height=5, bg="Grey", relief="flat",
            command=lambda: place_spot(self, 9, self.position_nine))

        self.position_one.grid(row=0, column=0, padx=2, pady=2)
        self.position_two.grid(row=0, column=1, padx=2, pady=2)
        self.position_three.grid(row=0, column=2, padx=2, pady=2)
        self.position_four.grid(row=1, column=0, padx=2, pady=2)
        self.position_five.grid(row=1, column=1, padx=2, pady=2)
        self.position_six.grid(row=1, column=2, padx=2, pady=2)
        self.position_seven.grid(row=2, column=0, padx=2, pady=2)
        self.position_eight.grid(row=2, column=1, padx=2, pady=2)
        self.position_nine.grid(row=2, column=2, padx=2, pady=2)

        def place_spot(self, position: int, widget) -> None:
            if self.turn == 9:
                return

            if widget["text"]:
                self.turn += 1

            row = ceil(position / 3) - 1
            col = (position + 2) % 3
            icon = "X" if self.turn % 2 == 0 else "O"
            self.matrix_field[row][col] = icon
            widget["text"] = icon
