'''

You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such
that all of these parts represent the same binary value. If it is possible, return any [i, j] with i + 1 < j,
such that: arr[0], arr[1], ..., arr[i] is the first part, arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part,
and arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part. All three parts have equal binary values. If it
is not possible, return [-1, -1]. Note that the entire part is used when considering what binary value it represents.
For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent
the same value.

Example 1:
Input: arr = [1,0,1,0,1]
Output: [0,3]

Example 2:
Input: arr = [1,1,0,1,1]
Output: [-1,-1]

Example 3:
Input: arr = [1,1,0,0,1]
Output: [0,2]

Constraints:
3 <= arr.length <= 3 * 104
arr[i] is 0 or 1
'''


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        def check_equal_division(a, l1, l2):
            while a[l1] == 0:
                l1 += 1
            while l2 < len(a):
                if a[l1] != a[l2]:
                    return -1
                else:
                    l1 += 1
                    l2 += 1
            return l1 - 1

        n = len(arr)
        one_count = 0
        for el in arr:
            if el == 1:
                one_count += 1
        if one_count % 3 != 0:
            return [-1, -1]
        if one_count == 0:
            return [0, n - 1]
        equal_one_count = one_count // 3
        third = 0
        count = 0
        # computing the third part
        for i in range(n - 1, -1, -1):
            if arr[i] == 1:
                count += 1
                if count == equal_one_count:
                    third = i
                    break
        # computing the first part
        first = check_equal_division(arr, 0, third)
        if first == -1:
            return [-1, -1]
        # Getting the second part
        second = check_equal_division(arr, first + 1, third)
        if second == -1:
            return [-1, -1]
        return [first, second + 1]
