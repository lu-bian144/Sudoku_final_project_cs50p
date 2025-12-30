board = [
         [9, 3, ".", ".", 7, ".", ".", ".", "."],
         [6, ".", ".", 1, 9, 5, ".", ".", "."],
         [".", 5, 8, ".", ".", ".", ".", 6, "."],
         [8, ".", ".", ".", 6, ".", ".", ".", 3],
         [4, ".", ".", 8, ".", 3, ".", ".", 1],
         [7, ".", ".", ".", 2, ".", ".", ".", 6],
         [".", 6, ".", ".", ".", ".", 2, 8, "."],
         [".", ".", ".", 4, 1, 9, ".", ".", 5],
         [".", ".", ".", ".", 8, ".", ".", 7, 9]
        ]
def main():
    tries=0
    while tries < 3:
        try:
            row = int(input("Enter row: ").strip()) #represented by a list
            column = int(input("Enter column: ").strip()) #represented by the index
            number= int(input("Pick a number in a range of 1-9: ").strip())
            if check_input(row, column, number):
                pass
            else:
                tries+=1
                print(f"Tries: {tries}")
                print("Input must be within a 1-9 range for all clauses!")
                continue
        except ValueError:
            tries+=1
            print(f"Tries: {tries}")
            print("Invalid input!")
            continue
        try:
            check_square(row-1, column-1, number)
            for j in check_row(board[row-1], number):
                if board[row-1].index(j) == check_column(column, number)-1:
                    board[row-1][column-1] = number
                    break
                else:
                    continue
        except ValueError:
            print("number already in row/column/square!")
            tries += 1
            
        for row in board:
            for k in row:
                print(k, end=" ")
            print()
        print(f"Tries: {tries}")
    print("Game over!")
    
def check_row(selected_r, selected_num):
    for i in selected_r:
        if selected_num == i:
            raise ValueError
    return selected_r
def check_column(selected_c, selected_num):
    for i in board:
        if i[selected_c-1] == selected_num:
            raise ValueError
    return selected_c
def check_square(selected_r, selected_c, selected_n):
    start_r = (selected_r//3)*3
    start_c = (selected_c//3)*3
    for i in range(start_r,start_r+3):
        for j in range(start_c, start_c+3):
            hi= board[i][j]
            if board[i][j]==selected_n:
                raise(ValueError)
           
    return True
def check_input(row, column, number):
    if 0 < row <=9 and 0 < column <=9 and 0 < number <=9 :
        return True
    else:
        return False
main()