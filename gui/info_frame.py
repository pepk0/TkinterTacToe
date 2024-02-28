from gui.image_frame import ImageFrame
from tkinter import Label


class InfoFrame(ImageFrame):
    """A class that gives game information"""

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
        img = self.image_O if parent.game.turn % 2 == 0 else self.image_X

        if draw:
            img = self.image_one
        elif element:
            img = self.image_O if element == "O" else self.image_X

        self.img_label["image"] = img
