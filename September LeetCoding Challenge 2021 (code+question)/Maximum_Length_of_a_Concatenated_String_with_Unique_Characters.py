'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
   Hide Hint #1
You can try all combinations and keep mask of characters you have.
   Hide Hint #2
You can use DP.
'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isDuplicate(s):
            cur = 0
            for i in s:
                val = ord(i) - ord('a')
                if cur & (1 << val) != 0:
                    return True
                cur = cur | (1 << val)
            return False

        def isDuplicate1(s):
            return len(s) != len(set(s))

        ans = 0
        n = len(arr)
        for m in range(0, 1 << n):
            s = ""
            for i in range(n):
                if m & (1 << i) != 0:
                    s = s + arr[i]
            if not isDuplicate1(s):
                ans = max(ans, len(s))
        return ans