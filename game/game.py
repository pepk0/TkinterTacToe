from prettytable import PrettyTable
from utils.functionality import get_coordinates


class TicTacToe:
    """A class imitating the Tic Tac Toe game and holing game specific
    functions such as check for winners, place piece and more"""

    def __init__(self) -> None:
        self.game_filed: list = [[0] * 3 for _ in range(3)]
        # this dict is used to map coordinates in the form row,
        # col to Frame objects
        self.mapping: dict = {}
        self.turn: int = 0
        self.score: dict = {}

    def place(self, element: str, position: int) -> bool:
        """Given a matrix of size 3x3, element(str) and position (integer),
        maps the position to row, col and places the element there"""
        row, col = get_coordinates(position)

        if self.game_filed[row][col] == 0:
            self.game_filed[row][col] = element
            return True

        return False

    def get_winner(self, position: int, element: str) -> list | None:
        """Given a matrix of size 3x3, position (int) and element (str)
        check if the current placed element, forms a wining chain"""
        row, col = get_coordinates(position)
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        cur_row, cur_col = row, col

        while directions:

            next_row, next_col = directions.pop()
            winner = [(cur_row, cur_col)]
            for i in range((3 * 2) - 2):

                if i == 3 - 1:
                    cur_row, cur_col = row, col
                    next_row, next_col = next_row * -1, next_col * -1

                cur_row, cur_col = next_row + cur_row, next_col + cur_col

                if 0 <= cur_row < 3 and 0 <= cur_col < 3:
                    if self.game_filed[cur_row][cur_col] == element:
                        winner.append((cur_row, cur_col))

                if len(winner) >= 3:
                    return winner

            cur_row, cur_col = row, col

        return None

    def write_results(self, winner: str) -> None:
        """Given a winner(string) takes set string and increments the
        result that winner"""

        self.score[winner] = self.score.get(winner, 0) + 1

    def display_result(self) -> str:
        """Formats the results in to a string table representation"""
        table = PrettyTable()

        table.field_names = ["Wins X", "Draws", "Wins O"]
        table.add_row([self.score.get("X", 0), self.score.get("Draw", 0),
                       self.score.get("O", 0)])

        return table.get_formatted_string(out_format="text")

    def finish_game(self) -> None:
        """When called this function fills up the game field with elements
        so we cant place after the game has finished"""
        self.game_filed = [["X"] * 3 for _ in range(3)]

    def reset_game(self) -> None:
        """"When called resets the game and clears
        the game filed in the main frame"""
        self.turn = 0
        self.game_filed: list = [[0] * 3 for _ in range(3)]
