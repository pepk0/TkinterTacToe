from tkinter import Tk
from game.game import TicTacToe
from gui.control_frame import ControlFrame
from gui.grid_position import GridPosition
from gui.info_frame import InfoFrame
from utils.functionality import get_coordinates, display_text, write_results


class MainFrame(Tk):
    """A class that displays all the information
    buttons and grids of the game"""

    def __init__(self) -> None:
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.game = TicTacToe()
        self.geometry('+%d+%d' % (700, 200))

        self.info_field = InfoFrame(img_size=40)
        self.control_field = ControlFrame(parent=self)

        self.control_field.grid(row=0, column=0, columnspan=3, pady=20)
        self.info_field.grid(row=1, column=0, columnspan=3)

        for number in range(1, 10):
            # places 9 frames making a 3x3 tic-tac-toe pattern
            grid_pos = GridPosition(number, img_size=80)
            row, col = get_coordinates(number)
            self.game.mapping[(row, col)] = grid_pos
            # dynamically calculate position
            # based on the number of the grid position
            grid_pos.grid(row=row + 2, column=col, padx=2, pady=2)
            # on click event binding instead of a button command
            grid_pos.button.bind("<Button-1>",
                                 lambda event, frame=grid_pos:
                                 self.on_button_click(frame))

    def on_button_click(self, frame: GridPosition) -> None:
        """places the correct element on the clicked 
        button and check's if it's a winning move"""
        position = frame.number
        element = "O" if self.game.turn % 2 == 0 else "X"

        if self.game.place(element, position):
            # place an appropriate image on the button and info panel
            frame.on_place(self)
            self.info_field.set_img(self)

            # try to find a winner
            winning_pos = self.game.get_winner(position, element)

            if winning_pos:
                write_results(element)
                self.game.mark_winner(winning_pos)
                display_text(self, self.info_field,
                             "The winner is: ", element=element)
                self.game.finish_game()
            # a maximum of 9 moves can be made
            # if no one has won by, then it's a draw
            elif self.game.turn == 9:
                write_results("Draw")
                display_text(self, self.info_field,
                             "Game Over! DRAW!", draw=True)
