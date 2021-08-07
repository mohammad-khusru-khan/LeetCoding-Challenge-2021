'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1

Constraints:
1 <= s.length <= 2000
s consists of lower-case English letters only.
'''

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut = [0] * (n + 1)
        for i in range(n + 1):
            cut[i] = i - 1
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j])
                j += 1
            j = 1
            while i - j + 1 >= 0 and i + j < n and s[i - j + 1] == s[i + j]:
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j + 1])
                j += 1
        return cut[n]