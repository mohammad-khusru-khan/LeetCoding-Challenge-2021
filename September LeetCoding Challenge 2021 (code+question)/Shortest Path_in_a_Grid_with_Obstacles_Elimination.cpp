/*
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] == 0 or 1
grid[0][0] == grid[m - 1][n - 1] == 0
   Hide Hint #1  
Use BFS.
   Hide Hint #2  
BFS on (x,y,r) x,y is coordinate, r is remain number of obstacles you can remove.
*/

class Solution
{
public:
    int shortestPath(vector<vector<int>> &grid, int k)
    {
        int M = grid.size(), N = grid[0].size(), steps = 0;
        const vector<int> dir{-1, 0, 1, 0, -1};
        vector<vector<vector<int>>> seen(M, vector<vector<int>>(N, vector<int>(k + 1)));
        queue<vector<int>> q{{{0, 0, 0}}};
        while (!q.empty())
        {
            int sz = q.size();
            while (sz-- > 0)
            {
                auto p = q.front();
                q.pop();
                if (p[0] == M - 1 && p[1] == N - 1)
                    return steps;
                for (int i = 0; i < 4; i++)
                {
                    int x = p[0] + dir[i], y = p[1] + dir[i + 1];
                    if (x < 0 || x >= M || y < 0 || y >= N)
                        continue;
                    int w = grid[x][y] + p[2];
                    if (w > k || seen[x][y][w])
                        continue;
                    seen[x][y][w] = 1;
                    q.push({x, y, w});
                }
            }
            steps++;
        }
        return -1;
    }
};