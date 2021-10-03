'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''


# 1st Solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        import itertools
        steps = list(itertools.accumulate([i + ele for i, ele in enumerate(nums)], max))
        return all(i != steps[i] for i in range(len(steps) - 1))


# 2nd Solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last:
                last = i
        if last == 0:
            return True
        else:
            return False
