from typing import List, Optional
from number_place.board import Board


def solve(board: List[List[Optional[int]]]) -> List[List[int]]:
    """
    数独を解く関数

    Args:
        board: 9x9の2次元配列。要素は1-9の整数またはNone

    Returns:
        List[List[int]]: 解かれた数独の盤面

    Raises:
        ValueError: 解けない場合
    """

    return _solve(Board(board))


def _solve(board: Board) -> List[List[int]]:
    """
    数独を解くための再帰的な補助関数。
    バックトラッキングアルゴリズムを使用して解を探索する。

    Args:
        board: 現在の盤面状態を表すBoardインスタンス

    Returns:
        List[List[int]]: 解かれた数独の盤面

    Raises:
        ValueError: 解が見つからない場合
    """

    empty_pos = board.find_empty_pos()
    if not empty_pos:
        # 空いているマスがない場合、盤面は完成している
        return board.values

    row, col = empty_pos
    for num in range(1, 9 + 1):
        if board.is_valid(row, col, num):
            new_board = board.replace_at(row, col, num)
            try:
                # 新しい盤面で再帰的に解を探索
                return _solve(new_board)
            except ValueError:
                # 解が見つからない場合、次の数字を試す
                continue

    # 全ての数字を試しても解が見つからない場合
    raise ValueError("数独を解くことができません")
