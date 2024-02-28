from tkinter import Frame
from PIL import Image, ImageTk
import os
from abc import ABC, abstractmethod


class ImageFrame(ABC, Frame):
    """A class that contains all the images as attributes used in the game."""

    @abstractmethod
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
