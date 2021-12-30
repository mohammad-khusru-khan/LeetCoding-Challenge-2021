'''
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

 

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.
 

Constraints:

1 <= k <= 105
'''
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k % 2 or not k % 5:
            return -1
        re, l = 1, 1
        while True:
            re %= k
            if not re:
                return l
            l += 1
            re = 10 * re + 1