/*
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 
Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
*/

class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        sort(nums.begin(), nums.end());
        int n = nums.size(), max_sum = 100001;
        int i, j, start, end;
        for (i = 0; i < n - 2; i++)
        {
            start = i + 1;
            end = n - 1;
            while (start < end)
            {
                int sum = nums[i] + nums[start] + nums[end];
                if (abs(target - sum) < abs(target - max_sum))
                    max_sum = sum;
                else if (sum > target)
                    end--;
                else
                    start++;
            }
        }
        return max_sum;
    }
};