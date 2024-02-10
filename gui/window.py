import tkinter as tk
from tkinter import ttk


class ButtonFrame(tk.Frame):
    def __init__(self) -> None:
        super().__init__()
        self.new_button = ttk.Button(self, text="New Game", width=20)
        self.quit_button = ttk.Button(self, text="Quit")

        self.new_button.grid(row=0, column=0, padx=5)
        self.quit_button.grid(row=0, column=1)


class MainFrame(tk.Tk):
    def __init__(self, ) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("350x350")
        self.resizable(False, False)
        self.option_frame = ButtonFrame().grid(row=0, column=0)
