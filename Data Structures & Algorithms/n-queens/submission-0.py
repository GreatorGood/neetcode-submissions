from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)
        queens = [-1] * n

        def backtrack(row: int):
            if row == n:
                board_snapshot = []
                for q_col in queens:
                    row_str = ["."] * n
                    row_str[q_col] = "Q"
                    board_snapshot.append("".join(row_str))
                solutions.append(board_snapshot)
                return

            for col in range(n):
                d1_id = row - col + n - 1
                d2_id = row + col

                if cols[col] or diag1[d1_id] or diag2[d2_id]:
                    continue

                queens[row] = col
                cols[col] = diag1[d1_id] = diag2[d2_id] = True

                backtrack(row + 1)

                cols[col] = diag1[d1_id] = diag2[d2_id] = False

        backtrack(0)
        return solutions
