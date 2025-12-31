# Sudoku Game – CS50P Final Project

---

## Video Demo: <https://www.youtube.com/watch?v=8BZeoB5uAC0>

---

## Description
This project is a command-line Sudoku game written in Python.  
The player interacts with a 9×9 Sudoku board by choosing a row, column, and number to place on the board.  
The program validates each move according to Sudoku rules and limits the number of invalid attempts.

This project was developed as a final project for **CS50P** and focuses on:
- Lists of lists
- Input validation
- Error handling with exceptions
- Game logic
- Modular function design

---

## Features
- 9×9 Sudoku board represented as a list of lists
- Manual user input for row, column, and number
- Validation for:
  - Row validation
  - Column validation
  - Subgrid square validation
- Limited number of attempts
- Console display of the board after each move
- Handling of invalid input

---

## Main file
- Contains a main function which handles the integration of the program and 5 additional ones that check status of the board, user input, and winning validation for the game
- check_row() and check_column() both iterate over the horizontal and vertical lines of the board, returning True or raising a ValueError
- check_square() divides the grid in subgroups, and iterates over the one containing the given coordinates, returning True or raising a ValueError
- check_input() checks that the user's input stays within the 1-9 range
- check_win() iterates over the whole board to find dots, if there are not any left it returns True, otherwise returns False

---

## Testing
- Condensed in a file called test_project.py
- Checks valid and invalid cases for each function and corner cases such as negative and out of range 

---

## Modules
- Tabulate library used for board styling, per the https://pypi.org/project/tabulate/ documentation

---

## Upcoming features
- Level system
- Random board generator
- GUI implementation

---

## How to Run
1. Make sure you have **Python 3** installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/lu-bian144/Sudoku_final_project_cs50p.git

