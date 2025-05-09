from dataclasses import dataclass
from typing import List, Optional, Self, Tuple

BOARD_SIZE = 9
BOARD_BOX_SIZE = 3


@dataclass
class Board:
    values: List[List[Optional[int]]]

    def replace_at(self, row: int, col: int, v: Optional[int]) -> Self:
        new_values = [r[:] for r in self.values]
        new_values[row][col] = v
        return Board(new_values)

    def is_valid(self, row: int, col: int, num: int) -> bool:
        """
        指定された位置に数字を配置できるかチェックする

        Args:
            row: 行番号
            col: 列番号
            num: 配置する数字

        Returns:
            bool: 配置可能な場合はTrue
        """
        # 行のチェック
        for x in range(BOARD_SIZE):
            if self.values[row][x] == num:
                return False

        # 列のチェック
        for x in range(BOARD_SIZE):
            if self.values[x][col] == num:
                return False

        # 3x3のボックスのチェック
        start_row = row - row % BOARD_BOX_SIZE
        start_col = col - col % BOARD_BOX_SIZE
        for i in range(BOARD_BOX_SIZE):
            for j in range(BOARD_BOX_SIZE):
                if self.values[i + start_row][j + start_col] == num:
                    return False

        return True

    def find_empty_pos(self) -> Optional[Tuple[int, int]]:
        """
        空いているマスを探す

        Returns:
            Optional[Tuple[int, int]]: 空いているマスの座標。見つからない場合はNone
        """
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.values[i][j] is None:
                    return (i, j)
        return None
