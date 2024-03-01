import os
import json
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
        # path to the location of the json file holding the results
        self.results_path: str = os.path.join("results", "results.json")

    def place(self, element: str, position: int) -> bool:
        """Given a matrix of size 3x3, element(str) and position (integer),
        maps the position to row, col and places the element there"""
        row, col = get_coordinates(position)

        if self.game_filed[row][col] == 0:
            self.game_filed[row][col] = element
            return True

        return False

    def get_winner(self, position: int, element: str) -> list | None:
        """ Given a matrix of size 3x3, position (int) and element (str)
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
        result json file for that winner"""

        with open(self.results_path) as json_file:
            curr_results = json.load(json_file)

            curr_results[winner] += 1

        with open(self.results_path, "w") as json_file:
            json.dump(curr_results, json_file, indent=4)

    def clear_results(self) -> None:
        """When called, this function will set all the results to 0"""

        with open(self.results_path) as json_file:
            curr_results = json.load(json_file)

            for item in curr_results:
                curr_results[item] = 0

        with open(self.results_path, "w") as json_file:
            json.dump(curr_results, json_file, indent=4)

    def finish_game(self) -> None:
        """when called this function fills up the game fild with elements
        so we cant place after the game has finished"""
        self.game_filed = [["X"] * 3 for _ in range(3)]
