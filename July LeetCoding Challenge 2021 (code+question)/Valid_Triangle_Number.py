'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:
Input: nums = [4,2,3,4]
Output: 4
'''


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count, n = 0, len(nums)
        for i in range(0, n - 2):
            k = i + 2
            for j in range(i + 1, n):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                if k > j:
                    count += k - j - 1
        return count
