'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

'''

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1e9 + 7
        dp = [[0 for i in range(5)] for j in range(n + 1)]
        for i in range(5):
            dp[1][i] = 1
        relation = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
        for i in range(1, n, 1):
            for u in range(5):
                dp[i + 1][u] = 0
                for v in relation[u]:
                    dp[i + 1][u] += dp[i][v] % MOD
        ans = 0
        for i in range(5):
            ans = (ans + dp[n][i]) % MOD
        return int(ans)
