from typing import Tuple, List
from functools import reduce
from operator import iconcat


def read_input() -> Tuple[List[int], List[List[List[Tuple[int, bool]]]]]:
    with open("inputs/day04.txt", "r") as f:
        lines = f.read().splitlines()

        numbers = list(map(int, lines[0].split(",")))

        boards = []

        current_board = []
        for line in lines[2:]:
            if len(line) == 0:
                boards.append(current_board)
                current_board = []
                continue

            row_numbers = list(map(int, line.strip().replace("  ", " ").split(" ")))
            row_numbers = list(map((lambda x: (x, False)), row_numbers))

            current_board.append(row_numbers)

        boards.append(current_board)

        return numbers, boards


def take_col(board, i):
    cols = []

    for row in board:
        cols.append(row[i])

    return cols


def board_wins(board) -> bool:
    rows = len(board)
    cols = len(board[0])

    for row_i in range(0, rows):
        row_matches = list(filter(lambda v: v[1] is True, board[row_i]))

        if len(row_matches) == cols:
            print(f"Winning row {row_matches}")
            return True

    for col_i in range(0, cols):
        column = take_col(board, col_i)

        col_matches = list(filter(lambda v: v[1] is True, column))

        if len(col_matches) == rows:
            print(f"Winning column {col_matches}")
            return True

    return False

def play_bingo(numbers, boards):
    for number in numbers:
        for board in boards:
            for board_row in board:
                for i in range(0, len(board_row)):
                    if board_row[i][0] == number:
                        board_row[i] = (number, True)

            # check for bingo
            if board_wins(board):
                return board, number

def score_board(board, last_number):
    flat_board = reduce(iconcat, board, [])
    unmarked_numbers = filter(lambda n: n[1] is False, flat_board)
    sum_of_unmarked = sum(map(lambda n: n[0], unmarked_numbers))

    return sum_of_unmarked * last_number

def part1():
    numbers, boards = read_input()

    winning_board, last_number = play_bingo(numbers, boards)
    print(f"Number {last_number} Winning board {winning_board}")

    score = score_board(winning_board, last_number)
    print(f"Board score is {score}")


part1()