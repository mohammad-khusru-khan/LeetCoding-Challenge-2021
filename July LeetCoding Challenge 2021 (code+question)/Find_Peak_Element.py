'''
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
'''


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def findpeak(nums, low, high, limit):
            mid = (low + high) // 2
            # checking the corner cases and the initial given condition
            if (mid == 0 or nums[mid - 1] <= nums[mid]) and (mid == limit - 1 or nums[mid + 1] <= nums[mid]):
                return mid
            # checking in the left half of the list
            elif mid > 0 and nums[mid - 1] >= nums[mid]:
                return findpeak(nums, low, mid - 1, limit)
            # checking in the right half of the list
            else:
                return findpeak(nums, mid + 1, high, limit)

        return findpeak(nums, 0, len(nums) - 1, len(nums))