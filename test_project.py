from project import check_row, check_column, check_square, check_input, check_win, board
import pytest


def test_valid_input():
    assert check_input(2, 2, 2) == True
    assert check_input(7, 2, 9) == True
    assert check_input(5, 9, 1) == True


def test_invalid_input():
    assert check_input(2, 4, 12) == False
    assert check_input(-1, 2, 3) == False
    assert check_input(45, 12, 1) == False


def test_valid_row():
    assert check_row(board[5], 9) == True
    assert check_row(board[8], 2) == True
    assert check_row(board[2], 5) == True


def test_invalid_row():
    with pytest.raises(ValueError):
        check_row(board[8], 9)
    with pytest.raises(ValueError):
        check_row(board[7], 5)
    with pytest.raises(ValueError):
        check_row(board[0], 7)


def test_valid_column():
    assert check_column(8, 2) == True
    assert check_column(0, 1) == True
    assert check_column(5, 1) == True


def test_invalid_column():
    with pytest.raises(ValueError):
        check_column(5, 9)
    with pytest.raises(ValueError):
        check_column(2, 8)
    with pytest.raises(ValueError):
        check_column(8, 1)


def test_valid_square():
    assert check_square(0, 8, 2) == True
    assert check_square(2, 1, 2) == True
    assert check_square(2, 5, 2) == True


def test_invalid_square():
    with pytest.raises(ValueError):
        check_square(1, 1 ,9)
    with pytest.raises(ValueError):
        check_square(3, 3, 8)
    with pytest.raises(ValueError):
        check_square(7, 7, 2)

def test_invalid_win():
    assert check_win() == False
