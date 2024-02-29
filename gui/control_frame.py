from tkinter import Frame, Button, Toplevel, Label
from utils.functionality import display_result


class ControlFrame(Frame):
    """A class that stores the buttons that control the game"""

    def __init__(self, parent) -> None:
        super().__init__()
        self.quit_button = Button(
            self, text="Quit Game", bg="#d15e6a", command=self.quit_game)
        self.restart_button = Button(
            self, text="Reset Game", command=self.reset_game)
        self.results_button = Button(self, text="Results",
                                     command=self.show_results)
        self.results_button.grid(row=0, column=0)
        self.restart_button.grid(row=0, column=1, padx=10)
        self.quit_button.grid(row=0, column=2)
        self.parent = parent

    def quit_game(self) -> None:
        """quits the game"""
        self.parent.game.clear_results()
        raise SystemExit

    def reset_game(self) -> None:
        """will destroy the current window"""
        self.parent.destroy()

    def show_results(self) -> None:
        top = Toplevel(self.parent)
        top.title("Results")
        top.geometry('+%d+%d' % (400, 200))
        top.resizable(False, False)
        Label(top, text=display_result(),
              font=("Consolas", 15)).grid(row=0, column=0)
