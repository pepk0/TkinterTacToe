from math import ceil


def get_coordinates(position: int) -> tuple:
    """Given a position(int) returns the matrix
    coordinates(row, col) for this grid position"""
    return ceil(position / 3) - 1, (position + 2) % 3


def get_winner(matrix: list, position: int, element: str) -> list | None:
    """ Given a matrix of size 3x3, position (int) and element (str)
    check if the current placed element, forms a wining chain in length of 3"""
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
    """Given a matrix of size 3x3, element(str) and position (integer),
    maps the position to row, col and places the element there"""
    row, col = get_coordinates(position)

    if matrix[row][col] == 0:
        matrix[row][col] = element
        return True

    return False


def mark_winner(winning_sequence: list, mapping: dict) -> None:
    """Given the winning sequence list[(int, int)…] and a
    mapping dict{(int, int): tk.Frame} takes each frame object and sets its
    background color to green to mark winning positions"""
    for winner in winning_sequence:
        mapping[winner].button["bg"] = "Green"
        mapping[winner].button["activebackground"] = "Green"


def display_text(parent, widget, text: str, draw=False, element=None) -> None:
    """Given a text(string) a boolean and a widget(tk.Frame) takes the widget
    and places the text on it and sets the appropriate image"""
    widget.text_label["text"] = text
    widget.set_img(parent, draw=draw, element=element)
