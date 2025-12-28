board = [
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [2, 3, 4, 5, 6, 7, 8, 9, 1],
         [3, 4, 5, 6, 7, 8, 9, 1, 2],
         [4, 5, 6, 7, 8, 9, 1, 2, 3],
         [5, 6, 7, 8, 9, 1, 2, 3, 4],
         [6, 7, 8, 9, 1, 2, 3, 4, 5],
         [7, 8, 9, 1, 2, 3, 4, 5, 6],
         [8, 9, 1, 2, 3, 4, 5, 6, 7],
         [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]
def main():
    row = int(input("Enter row: ").strip()) #represented by a list
    column = int(input("Enter column: ").strip()) #represented by the index
    number= int(input("Pick a number in a range of 1-9: ").strip())
    for j in board[row-1]:
        if board[row-1].index(j) == column-1:
            board[row-1][column-1] = number
    for i in board:
        print(i)
def check_row():
    ...
def check_column():
    ...
def check_square():
    ...

main()