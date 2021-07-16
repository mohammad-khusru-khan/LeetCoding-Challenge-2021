'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                start = j + 1
                end = n - 1
                while start < end:
                    sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if sum < target:
                        start += 1
                    elif sum > target:
                        end -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
        return ans
