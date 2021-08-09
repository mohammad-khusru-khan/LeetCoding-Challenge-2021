'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        n1, n2 = len(num1), len(num2)
        dif = n1 - n2
        ans = ''
        carry = 0
        for i in range(n2 - 1, -1, -1):
            sum_ = (ord(num1[i + dif]) - ord('0')) + (ord(num2[i]) - ord('0')) + carry
            ans += str(sum_ % 10)
            carry = sum_ // 10
        for i in range(n1 - n2 - 1, -1, -1):
            sum_ = (ord(num1[i]) - ord('0')) + carry
            ans += str(sum_ % 10)
            carry = sum_ // 10
        if carry:
            ans += str(carry)
        ans = ans[::-1]
        return ans