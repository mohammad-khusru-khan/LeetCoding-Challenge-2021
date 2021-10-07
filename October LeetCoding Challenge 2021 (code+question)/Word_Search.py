'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(word, i, j, m, n):
            if board[i][j] != word[self.l]:
                return
            visited.add((i, j))
            self.l += 1
            if self.l == len(word):
                self.is_found = True
                return
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i1, j1 = i + di, j + dj
                if 0 <= i1 < m and 0 <= j1 < n and (i1, j1) not in visited:
                    backtrack(word, i1, j1, m, n)
                    if self.is_found:
                        return
            visited.remove((i, j))
            self.l -= 1

        if not board or not board[0]:
            return False
        if word == '':
            return True
        m, n = len(board), len(board[0])
        self.is_found = False
        self.l = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                backtrack(word, i, j, m, n)
                if self.is_found:
                    return True
        return False
