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


def write_results(winner: str) -> None:
    """Given a winner(string) takes set string and increments the
    result json file for that winner"""
    json_path = os.path.join("results", "results.json")

    with open(json_path) as f:
        curr_results = json.load(f)

        curr_results[winner] += 1

    with open(json_path, "w") as f:
        json.dump(curr_results, f, indent=4)


def clear_results() -> None:
    """When called, this function will set all the results to 0"""
    json_path = os.path.join("results", "results.json")

    with open(json_path) as f:
        curr_results = json.load(f)

        for item in curr_results:
            curr_results[item] = 0

    with open(json_path, "w") as f:
        json.dump(curr_results, f, indent=4)


def display_result() -> str:
    """Formats the results in to a string table representation"""
    json_path = os.path.join("results", "results.json")
    table = PrettyTable()

    with open(json_path) as f:
        results = json.load(f)

    table.field_names = ["Wins X", "Draws", "Wins O"]
    table.add_row([results["X"], results["Draw"], results["O"]])

    return table.get_formatted_string(out_format="text")
