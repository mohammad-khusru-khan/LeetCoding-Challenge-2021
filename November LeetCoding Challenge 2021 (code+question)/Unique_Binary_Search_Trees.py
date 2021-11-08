'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19
'''
class Solution:
    def numTrees(self, n: int) -> int:
        
        def comb(n, r):
            ans = 1
            for i in range(r):
                ans *= (n - i)
                ans //= (i + 1)
            return ans
        
        return comb(2 * n, n) // (n + 1)