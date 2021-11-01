'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col):
            board[row][col] = "Z"
            for dr, dc in (-1, 0), (0, 1), (1, 0), (0, -1):
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] != 'O':
                    continue
                dfs(nr, nc)

        def flip():
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == "Z":
                        board[row][col] = "O"
                    elif board[row][col] == "O":
                        board[row][col] = "X"

        for row in [0, rows - 1]:
            for col in range(cols):
                if board[row][col] == 'O':
                    dfs(row, col)

        for col in [0, cols - 1]:
            for row in range(1, rows - 1):
                if board[row][col] == 'O':
                    dfs(row, col)

        flip()