'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
                return False
            c = board[i][j]
            board[i][j] = '$'
            s = word[1:]
            res = dfs(board, i - 1, j, s) or dfs(board, i + 1, j, s) or dfs(board, i, j - 1, s) or dfs(board, i, j + 1,
                                                                                                       s)
            board[i][j] = c
            return res

        ans = []
        for x in words:
            p = 0
            rev = x[::-1]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if dfs(board, i, j, rev):
                        p = 1
                        break
                if p:
                    break
            if p:
                ans.append(x)
        return ans