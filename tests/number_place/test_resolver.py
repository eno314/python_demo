import pytest
from number_place import solver
from number_place.board import Board

base_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


@pytest.mark.parametrize(
    "board",
    [
        base_board,
        Board(base_board).replace_at(0, 0, None).values,
        Board(base_board)
        .replace_at(0, 0, None)
        .replace_at(0, 1, None)
        .replace_at(1, 0, None)
        .replace_at(1, 1, None)
        .replace_at(8, 8, None)
        .replace_at(8, 7, None)
        .replace_at(7, 8, None)
        .replace_at(7, 7, None)
        .replace_at(0, 8, None)
        .values,
    ],
)
def test_solve_happy_path(board):
    assert solver.solve(board) == base_board


def test_hard_board():
    board = [
        [None, None, 9, None, 7, None, None, 3, 5],
        [5, 1, None, None, 4, None, 2, None, 6],
        [7, None, None, None, None, 6, None, None, 1],
        [6, None, None, None, None, 7, None, 9, 3],
        [None, 2, 3, None, 1, None, None, None, None],
        [None, None, 1, None, None, None, 5, None, None],
        [8, None, None, None, None, None, None, 4, 9],
        [1, 9, None, None, None, None, None, 5, 8],
        [None, None, 7, None, None, None, 6, None, None],
    ]
    assert solver.solve(board) == [
        [2, 6, 9, 8, 7, 1, 4, 3, 5],
        [5, 1, 8, 3, 4, 9, 2, 7, 6],
        [7, 3, 4, 2, 5, 6, 9, 8, 1],
        [6, 8, 5, 4, 2, 7, 1, 9, 3],
        [4, 2, 3, 9, 1, 5, 8, 6, 7],
        [9, 7, 1, 6, 8, 3, 5, 2, 4],
        [8, 5, 6, 1, 3, 2, 7, 4, 9],
        [1, 9, 2, 7, 6, 4, 3, 5, 8],
        [3, 4, 7, 5, 9, 8, 6, 1, 2],
    ]
