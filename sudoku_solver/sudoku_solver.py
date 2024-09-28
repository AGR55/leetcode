from time import time


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def isValid(r: int, c: int, n: str) -> bool:
            for i in range(9):
                if board[i][c] == n or board[r][i] == n:
                    return False

                subgrid_row = 3 * (r // 3) + i // 3
                subgrid_col = 3 * (c // 3) + i % 3
                if board[subgrid_row][subgrid_col] == n:
                    return False
            return True

        def fill(r: int, c: int) -> bool:
            if r == 9:
                return True
            if c == 9:
                return fill(r + 1, 0)

            if board[r][c] == '.':
                for k in range(1, 10):
                    if isValid(r, c, str(k)):
                        board[r][c] = str(k)

                        if fill(r, c + 1):
                            return True

                        board[r][c] = '.'

                return False

            return fill(r, c + 1)

        fill(0, 0)
        return board


def main():
    solution = Solution()
    time_start = time()
    print(*solution.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]), sep='\n')
    time_end = time()
    print()
    print(f'Tiempo de ejecucion: {time_end - time_start}')


if __name__ == '__main__':
    main()
