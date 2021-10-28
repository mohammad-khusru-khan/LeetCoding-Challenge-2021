'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        nums.sort()
        n = len(nums)
        flag = False
        for i in range(n - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                start = i + 1
                end = n - 1
                target = 0 - nums[i]
                while start < end:
                    if start > i + 1 and nums[start] == nums[start - 1]:
                        start += 1
                        continue
                    if end < n - 1 and nums[end] == nums[end + 1]:
                        end -= 1
                        continue
                    if target == nums[start] + nums[end]:
                        ans.append([nums[i], nums[start], nums[end]])
                        flag = True
                        start += 1
                        end -= 1
                    elif target > (nums[start] + nums[end]):
                        start += 1
                    else:
                        end -= 1
        return ans 