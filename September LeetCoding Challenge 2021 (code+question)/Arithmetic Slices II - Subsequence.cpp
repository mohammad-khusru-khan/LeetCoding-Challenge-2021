/*
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

 

Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.
 

Constraints:

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
*/
typedef long long int lli;
class Solution
{
public:
    int numberOfArithmeticSlices(vector<int> &nums)
    {
        int ret = 0;
        unordered_map<lli, unordered_map<lli, lli>> dp, cnt;
        unordered_set<int> s(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 1; i < n; i++)
        {
            for (int j = i - 1; j >= 0; j--)
            {
                lli diff = (lli)nums[i] - (lli)nums[j];
                if (diff <= INT_MIN || diff > INT_MAX)
                    continue;
                int temp = dp[j].count(diff) ? dp[j][diff] : 0;
                ret += temp;
                if (s.count(nums[i] + diff))
                    dp[i][diff] += temp + 1;
            }
        }
        return ret;
    }
};