'''
Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.



Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []


Constraints:

1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
   Hide Hint #1
Note that a number can contain multiple digits.
   Hide Hint #2
Since the question asks us to find all of the valid expressions, we need a way to iterate over all of them. (Hint: Recursion!)
   Hide Hint #3
We can keep track of the expression string and evaluate it at the very end. But that would take a lot of time. Can we keep track of the expression's value as well so as to avoid the evaluation at the very end of recursion?
   Hide Hint #4
Think carefully about the multiply operator. It has a higher precedence than the addition and subtraction operators.
1 + 2 = 3
1 + 2 - 4 --> 3 - 4 --> -1
1 + 2 - 4 * 12 --> -1 * 12 --> -12 (WRONG!)
1 + 2 - 4 * 12 --> -1 - (-4) + (-4 * 12) --> 3 + (-48) --> -45 (CORRECT!)
   Hide Hint #5
We simply need to keep track of the last operand in our expression and reverse it's effect on the expression's value while considering the multiply operator.

'''


class Solution:
    def search(self, num, eq, last, cur, target, res):
        if len(num) == 0:
            if cur == target:
                res.append(eq)
        else:
            for i in range(1, len(num) + 1):
                n = num[0:i]
                if len(n) > 1 and n[0] == '0':
                    return

                if len(eq) > 0:
                    self.search(num[i:], eq + '+' + n, int(n), cur + int(n), target, res)
                    self.search(num[i:], eq + '-' + n, -int(n), cur - int(n), target, res)
                    self.search(num[i:], eq + '*' + n, last * int(n), (cur - last) + (last * int(n)), target, res)
                else:
                    self.search(num[i:], n, int(n), int(n), target, res)

    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.search(num, "", 0, 0, target, res)
        return res