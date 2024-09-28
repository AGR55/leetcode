from time import time

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def is_valid(conjunto: set, value: str) -> bool:
            if value != '.':
                if value not in conjunto:
                    conjunto.add(value)
                    return True
                return False
            return True

        for row in range(9):
            row_set, col_set, block_set = set(), set(), set()
            for col in range(9):
                if not (is_valid(row_set, board[row][col]) and is_valid(col_set, board[col][row])):
                    return False

                block_row, block_col = (col // 3) + (3 * (row // 3)), (col % 3) + (3 * (row % 3))
                if not is_valid(block_set, board[block_row][block_col]):
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    start_time = time()
    print(s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                           [".", "9", "8", ".", ".", ".", ".", "6", "."],
                           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                           [".", "6", ".", ".", ".", ".", "2", "8", "."],
                           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    end_time = time()
    print(f'Time execution: {end_time - start_time}')
