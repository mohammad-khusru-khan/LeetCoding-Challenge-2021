'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
   Hide Hint #1
Count the frequency of letters in the given string.
   Hide Hint #2
Find the letter than can make the minimum number of instances of the word "balloon".
'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b, a, l, o, n = 0, 0, 0, 0, 0
        for i in text:
            if i == 'b':
                b += 1
            elif i == 'a':
                a += 1
            elif i == 'l':
                l += 1
            elif i == 'o':
                o += 1
            elif i == 'n':
                n += 1
        l //= 2
        o //= 2
        return min(b, a, l, o, n)
