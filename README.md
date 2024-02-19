# TkinterTacToe:
> This is the classical game Tic Tac Toe implemented in the tkinter package (“Tk interface”) Python interface to the Tcl/Tk GUI toolkit GUI library.

# How to play the game:    
  The goal of the game is to connect horizontally vertically or diagonally 3 of either "X" or "O", if all cells are filled up and no one was able to connect 3 elements a draw occurs.  

## Demonstration:
![game_play](https://i.imgur.com/HntJa5A.gif)


## Game Menu:
  The game menu consists of two buttons:

  1. ### Reset game Button:
      The reset game option is used to reset the game (closing the main root, which is in a while True loop and will start over again as if the game is resting.)  
      ![reset_button](https://i.imgur.com/h883cni.gif)  
      **NOTE: To exit use Quit Game**
  
  2. ### Quit Game Button:
      Exits the game.. for real (the X button doesn't work, raising a SystemExit exception the quit game button closes the program and doesn't let the while loop restart the root.)  
      ![quit_button](https://i.imgur.com/lZvi4jt.gif)  

## How to run:

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
