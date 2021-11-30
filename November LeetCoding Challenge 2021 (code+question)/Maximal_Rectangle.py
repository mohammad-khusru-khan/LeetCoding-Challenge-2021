'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0
 

Constraints:

rows == matrix.length
cols == matrix[i].length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if not rows:
            return 0
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            acc = 0
            for j in range(cols):
                if matrix[i][j] == '1':
                    acc += 1
                else:
                    acc = 0
                dp[i][j] = acc
        res = 0
        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                bSide, rSide = dp[i][j], 0
                k = i
                while k > -1 and dp[k][j]:
                    bSide = min(bSide, dp[k][j])
                    rSide += 1
                    res = max(res, bSide * rSide)
                    k -= 1
        return res