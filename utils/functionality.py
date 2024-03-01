from math import ceil


def get_coordinates(position: int) -> tuple:
    """Given a position(int) returns the matrix
    coordinates(row, col) for this grid position"""
    return ceil(position / 3) - 1, (position + 2) % 3


def display_text(parent, widget, text: str, draw=False, element=None) -> None:
    """Given a text(string) a boolean and a widget(tk.Frame) takes the widget
    and places the text on it and sets the appropriate image"""
    widget.text_label["text"] = text
    widget.set_img(parent, draw=draw, element=element)


def mark_winner(winning_sequence: list, mapping: dict) -> None:
    """Given the winning sequence list[(int, int)…] and a
    mapping dict{(int, int): tk.Frame} takes each frame object and sets its
    background color to green to mark winning positions"""
    for winner in winning_sequence:
        mapping[winner].button["bg"] = "Green"
        mapping[winner].button["activebackground"] = "Green"


def get_element(turn: int, first_element, second_element):
    """"Given two elements and a turn(int) gives back the first element
    if the turn is even and the second element if the turn is odd"""
    return first_element if turn % 2 == 0 else second_element
