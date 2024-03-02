# TkinterTacToe:

This is the classical game Tic Tac Toe implemented in the tkinter package (“Tk
interface”) Python interface to the Tcl/Tk GUI toolkit GUI library.

## Demonstration:

This is the basic gameplay, showing the functions and the looks of the game.

![game_play](https://i.imgur.com/ODMuCtE.gif)

# How to play the game:

The goal of the game is to connect horizontally,
vertically or diagonally 3 of either "X" or "O"
if all cells are filled up and no one was able to connect 3 elements
a draw occurs.

| **Game Interface**                                  | **Winning Condition** |
|-----------------------------------------------------|-----------------------|
| ![vertical win](https://i.imgur.com/FdTKv2O.jpeg)   | Vertical              |
| ![diagonal win](https://i.imgur.com/eC7TVCV.jpeg)   | Diagonal              |
| ![horizontal win](https://i.imgur.com/caak1o0.jpeg) | Horizontal            |
| ![draw](https://i.imgur.com/q6EQ4Ch.jpeg)           | Draw                  |
   
## Game Menu:

The game menu consists of three buttons:

1. #### Reset game Button:
   Resets the game and clears all the previously placed elements.

2. #### Quit Game Button:
   Exits the game.

3. #### Results Button:
   Shows the results of the game in a table format.

## How to play:

1. Create and activate a virtual environment
    ~~~ powershell
    py install -m venv .venv
    ~~~

2. Install the requirement.txt
    ~~~ powershell
    pip install -r requirements.txt
    ~~~

3. Run the main.py file
    ~~~ powershell
    py main.py
    ~~~
