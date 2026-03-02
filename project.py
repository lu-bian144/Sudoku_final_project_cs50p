from tabulate import tabulate
from random import choice
from boards import first_level_board, second_level_board, third_level_board
def main():
   
    level = input("Choose a level from 1 to 3: ")
    match level:
        case "1":
            game_board = choice(first_level_board)
        case "2":
            game_board = choice(second_level_board)
        case "3":
            game_board = choice(third_level_board)
        case _:
            print("Invalid level")


    print(tabulate(game_board, tablefmt="fancy_grid"))


    tries = 0
    while True:
        if tries == 3:
            print("Game over!")
            break
        try:
            row = int(input("Enter row: ").strip())
            column = int(input("Enter column: ").strip())
            number = int(input("Pick a number in a range of 1-9: ").strip())
            if check_input(row, column, number):
                pass
            else:
                tries += 1
                print(f"Tries: {tries}")
                print("Input must be within a 1-9 range for all clauses!")
                continue
        except ValueError:
            tries += 1
            print(f"Tries: {tries}")
            print("Invalid input!")
            continue
        try:
            check_row(game_board[row-1], number)
            check_column(column-1, number, game_board)
            check_square(row-1, column-1, number, game_board)

            game_board[row-1][column-1] = number

        except ValueError:
            print("number already in row/column/square!")
            tries += 1
        print(tabulate(game_board, tablefmt="fancy_grid"))
        print(f"Tries: {tries}")
        if check_win(game_board):
            print("You win!, have a tutuca 🥜🥜🥜")
            break


def check_row(selected_r, selected_num):
    for i in selected_r:
        if selected_num == i:
            raise ValueError
    return True


def check_column(selected_c, selected_num, board):
    for i in board:
        if i[selected_c] == selected_num:
            raise ValueError

    return True


def check_square(selected_r, selected_c, selected_n, board):
    start_r = (selected_r//3)*3
    start_c = (selected_c//3)*3
    for i in range(start_r, start_r+3):
        for j in range(start_c, start_c+3):
            hi = board[i][j]
            if board[i][j] == selected_n:
                raise (ValueError)

    return True


def check_win(board):
    for r in board:
        for c in r:
            if c != " ":
                continue
            else:
                return False
    return True


def check_input(row, column, number):
    if 0 < row <= 9 and 0 < column <= 9 and 0 < number <= 9:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
