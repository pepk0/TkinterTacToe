import tkinter as tk
from tkinter import ttk


class MainFrame(tk.Tk):
    def __init__(self,) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("350x350")
