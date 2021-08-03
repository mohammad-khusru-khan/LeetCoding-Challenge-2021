'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        size = 1 << len(nums)
        for i in range(size):
            l = []
            for j in range(len(nums)):
                # if the set bit is 1 or not
                if i & (1 << j):
                    l.append(nums[j])
            if l not in ans:
                ans.append(l)
        return ans