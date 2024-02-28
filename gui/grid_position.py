from gui.image_frame import ImageFrame
from tkinter import Button


class GridPosition(ImageFrame):
    """A class that represents a grid position on the tic-tac-toe field"""

    def __init__(self, number: int, img_size: int) -> None:
        super().__init__(img_size)
        self.number = number

        self.button = Button(self, image=self.image_one, height=110,
                             width=110, background="Gray", border=0,
                             activebackground="Gray")

        self.button.grid(row=0, column=0)

    def on_place(self, parent) -> None:
        """Places either an X or O, image on the pressed
        frame box based on the turn"""
        img = self.image_O if parent.game.turn % 2 == 0 else self.image_X
        self.button["image"] = img
        parent.game.turn += 1