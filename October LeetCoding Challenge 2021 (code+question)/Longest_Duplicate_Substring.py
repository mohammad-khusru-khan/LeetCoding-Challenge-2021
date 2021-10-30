'''
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

 

Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""
 

Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.
'''

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def IfSame(i, j):
            curr = s[i:j]
            if curr in s[i + 1:]:
                return True
            return False
        
        i, j, max_curr = 0, 1, ''
        while i < len(s) and j < len(s):
            while IfSame(i, j):
                max_curr = s[i:j]
                j += 1
            i += 1
            j = i + len(max_curr)
            
        return max_curr