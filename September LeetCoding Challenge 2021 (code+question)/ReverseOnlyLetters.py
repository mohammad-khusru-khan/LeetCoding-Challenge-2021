'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.



Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
   Hide Hint #1
This problem is exactly like reversing a normal string except that there are certain characters that we have to simply skip. That should be easy enough to do if you know how to reverse a string using the two-pointer approach.
'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def isAlpha(x):
            if (65 <= ord(x) <= 90) or (97 <= ord(x) <= 122):
                return True
            else:
                return False

        lis = [x for x in s]
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not isAlpha(lis[start]):
                start += 1
            while start < end and not isAlpha(lis[end]):
                end -= 1
            if start < end and isAlpha(lis[start]) and isAlpha(lis[end]):
                lis[start], lis[end] = lis[end], lis[start]
                start += 1
                end -= 1
        ans = ''
        for x in lis:
            ans += x
        return ans