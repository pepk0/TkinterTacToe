from gui.image_frame import ImageFrame
from tkinter import Label

from utils.functionality import get_element


class InfoFrame(ImageFrame):
    """A class that displays game information
    such as who won and who is placing on the board"""

    def __init__(self, img_size: int) -> None:
        super().__init__(img_size)
        self.text_label = Label(
            self, text="Placing: ", font=("Helvetica", 25))
        self.img_label = Label(self, image=self.image_O, height=90)
        self.img_label.grid(row=0, column=1)
        self.text_label.grid(row=0, column=0)

    def set_img(self, parent, element=None, draw=False) -> None:
        """sets the appropriate image based on if the
        game is draw or one of O or X wins"""
        img = get_element(parent.game.turn, self.image_O, self.image_X)

        if draw:
            img = self.image_one
        elif element:
            img = get_element(parent.game.turn, self.image_X, self.image_O)

        self.img_label["image"] = img
