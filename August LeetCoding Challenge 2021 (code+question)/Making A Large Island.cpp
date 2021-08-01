/*
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
*/

class Solution
{
public:
    int largestIsland(vector<vector<int>> &grid)
    {
        int n = grid.size();
        vector<int> vCount(2, 0);
        int number = 2;
        int maxNum = 1;
        for (int i = 0; i < grid.size(); i++)
            for (int j = 0; j < grid[i].size(); j++)
                if (grid[i][j] == 1)
                {
                    int others = 0;
                    int count = 0;
                    fun(grid, vCount, count, i, j, number, others);
                    number++;
                    vCount.push_back(count);
                    maxNum = max(maxNum, count + others + 1);
                }
        return maxNum > n * n ? n * n : maxNum;
    }

    void fun(vector<vector<int>> &g, vector<int> &vCount, int &count, int i, int j, int &number, int &others)
    {
        if (i < 0 || i == g.size() || j < 0 || j == g.size() || g[i][j] > 1)
            return;
        if (g[i][j] == 0)
        {
            int up(0), down(0), left(0), temp(0);
            if (i > 0 && g[i - 1][j] != number)
            {
                temp += vCount[g[i - 1][j]];
                up = g[i - 1][j];
            }
            if (i < g.size() - 1 && g[i + 1][j] != number && g[i + 1][j] != up)
            {
                temp += vCount[g[i + 1][j]];
                down = g[i + 1][j];
            }
            if (j > 0 && g[i][j - 1] != number && g[i][j - 1] != up && g[i][j - 1] != down)
            {
                temp += vCount[g[i][j - 1]];
                left = g[i][j - 1];
            }
            if (j < g.size() - 1 && g[i][j + 1] != number && g[i][j + 1] != up && g[i][j + 1] != down && g[i][j + 1] != left)
                temp += vCount[g[i][j + 1]];
            others = max(others, temp);
        }
        g[i][j] = number;
        count++;
        fun(g, vCount, count, i - 1, j, number, others);
        fun(g, vCount, count, i + 1, j, number, others);
        fun(g, vCount, count, i, j - 1, number, others);
        fun(g, vCount, count, i, j + 1, number, others);
    }
};