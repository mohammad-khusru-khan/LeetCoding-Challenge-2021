'''
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        def condition(row, coins_p):
            coins_n = row * (row + 1) // 2
            return coins_n <= coins_p
        
        start, end = 0, 65536
        res = 0
        while start <= end:
            mid =  start + (end - start) // 2
            if condition(mid, n):
                res = mid
                start = mid + 1
            else:
                end = mid - 1
                
        return res