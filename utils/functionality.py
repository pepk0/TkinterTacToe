from math import ceil


def get_coordinates(position: int) -> tuple:
    return ceil(position / 3) - 1, (position + 2) % 3


def get_winner(matrix: list, position: int, element: str) -> list | None:
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
                if matrix[cur_row][cur_col] == element:
                    winner.append((cur_row, cur_col))

            if len(winner) >= 3:
                return winner

        cur_row, cur_col = row, col

    return None


def place_on_matrix(matrix: list, element: str, position: int) -> bool:
    row, col = get_coordinates(position)

    if matrix[row][col] == 0:
        matrix[row][col] = element
        return True

    return False
