/*
You are given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left. 
Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.
Return the maximum points you can get.

Example 1:
Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)

Example 2:
Input: boxes = [1,1,1]
Output: 9

Example 3:
Input: boxes = [1]
Output: 1

Constraints:
1 <= boxes.length <= 100
1 <= boxes[i] <= 100
*/

class Solution
{
public:
    int removeBoxes(vector<int> &boxes)
    {
        int n = boxes.size();
        int dp[100][100][100] = {0};
        for (int i = 0; i < n; ++i)
        {
            for (int k = 0; k <= i; ++k)
            {
                dp[i][i][k] = (1 + k) * (1 + k);
            }
        }
        for (int t = 1; t < n; ++t)
        {
            for (int j = t; j < n; ++j)
            {
                int i = j - t;
                for (int k = 0; k <= i; ++k)
                {
                    int res = (1 + k) * (1 + k) + dp[i + 1][j][0];
                    for (int m = i + 1; m <= j; ++m)
                    {
                        if (boxes[m] == boxes[i])
                        {
                            res = max(res, dp[i + 1][m - 1][0] + dp[m][j][k + 1]);
                        }
                    }
                    dp[i][j][k] = res;
                }
            }
        }
        return n == 0 ? 0 : dp[0][n - 1][0];
    }
};