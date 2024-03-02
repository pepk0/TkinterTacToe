from tkinter import Frame, Button, Toplevel, Label


class ControlFrame(Frame):
    """A class that represents and holds the buttons that control the game"""

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
        """Quits the game"""
        raise SystemExit

    def reset_game(self) -> None:
        """Resets the game making it possible to place play again"""
        for _, grid_frame in self.parent.game.mapping.items():
            grid_frame.button["image"] = grid_frame.image_one
            grid_frame.button["height"] = grid_frame.GRID_HEIGHT
            grid_frame.button["width"] = grid_frame.GRID_WIDTH
            grid_frame.button["background"] = "Gray"
            grid_frame.button["activebackground"] = "Gray"

        self.parent.game.reset_game()
        self.parent.info_field.text_label["text"] = "Placing: "
        self.parent.info_field.set_img(self.parent)

    def show_results(self) -> None:
        """"Opens a new window displaying the results as a table"""
        top = Toplevel(self.parent)
        top.title("Results")
        top.geometry('+%d+%d' % (723, 380))
        top.resizable(False, False)
        Label(top, text=self.parent.game.display_result(),
              font=("Consolas", 15)).grid(row=0, column=0)
