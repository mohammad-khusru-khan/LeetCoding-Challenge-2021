'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        size = 9

        def number_unassigned(row, col):
            num_unassign = 0
            for i in range(0, size):
                for j in range(0, size):
                    # cell is unassigned
                    if board[i][j] == '.':
                        row = i
                        col = j
                        num_unassign = 1
                        a = [row, col, num_unassign]
                        return a
            a = [-1, -1, num_unassign]
            return a

        def is_safe(n, r, c):
            # checking in row
            for i in range(0, size):
                # there is a cell with same value
                if board[r][i] == n:
                    return False
            # checking in column
            for i in range(0, size):
                # there is a cell with same value
                if board[i][c] == n:
                    return False
            row_start = (r // 3) * 3
            col_start = (c // 3) * 3
            # checking subboard
            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if board[i][j] == n:
                        return False
            return True

        def Solve_Sudoku():
            row, column = 0, 0
            a = number_unassigned(row, column)
            if a[2] == 0:
                return True
            row, column = a[0], a[1]
            for i in range(1, 10):
                if is_safe(str(i), row, column):
                    board[row][column] = str(i)
                    if Solve_Sudoku():
                        return True
                    board[row][column] = '.'
            return False

        def print_sudoku():
            for i in board:
                for j in i:
                    print(j, end=' ')
                print()

        if Solve_Sudoku():
            print_sudoku()
