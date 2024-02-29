from math import ceil
import os
import json
from prettytable import PrettyTable


def get_coordinates(position: int) -> tuple:
    """Given a position(int) returns the matrix
    coordinates(row, col) for this grid position"""
    return ceil(position / 3) - 1, (position + 2) % 3


def display_text(parent, widget, text: str, draw=False, element=None) -> None:
    """Given a text(string) a boolean and a widget(tk.Frame) takes the widget
    and places the text on it and sets the appropriate image"""
    widget.text_label["text"] = text
    widget.set_img(parent, draw=draw, element=element)


def display_result() -> str:
    """Formats the results in to a string table representation"""
    json_path = os.path.join("results", "results.json")
    table = PrettyTable()

    with open(json_path) as f:
        results = json.load(f)

    table.field_names = ["Wins X", "Draws", "Wins O"]
    table.add_row([results["X"], results["Draw"], results["O"]])

    return table.get_formatted_string(out_format="text")


def mark_winner(winning_sequence: list, mapping: dict) -> None:
    """Given the winning sequence list[(int, int)…] and a
    mapping dict{(int, int): tk.Frame} takes each frame object and sets its
    background color to green to mark winning positions"""
    for winner in winning_sequence:
        mapping[winner].button["bg"] = "Green"
        mapping[winner].button["activebackground"] = "Green"
