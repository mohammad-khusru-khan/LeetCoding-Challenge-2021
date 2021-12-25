'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''
class Solution:
    def calculate(self, s: str) -> int:

        def calc(x, y, p =  True):
            if not p:
                for z in reversed(range(x, y + 1)):
                    if s[z] == '*':
                        return calc(x, z - 1) * calc(z + 1, y)
                    elif s[z] == '/':
                        return calc(x, z - 1) // calc(z + 1, y)
                return int(s[x : y + 1])
            else:
                for z in reversed(range(x, y + 1)):
                    if s[z] == '+':
                        return calc(x, z - 1) + calc(z + 1, y)
                    elif s[z] == '-':
                        return calc(x, z - 1) - calc(z + 1, y)
                return calc(x, y, p = False)
        return calc(0, len(s) - 1)