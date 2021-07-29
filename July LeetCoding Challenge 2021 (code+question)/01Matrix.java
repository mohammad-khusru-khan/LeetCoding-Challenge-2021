/*
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 
Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
*/

class Solution
{
public int[][] updateMatrix(int[][] mat)
    {
        int r = mat.length;
        int c = mat[0].length;

        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                if (mat[i][j] == 0)
                {
                    q.offer(new int[]{i, j});
                }
                else
                {
                    mat[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        int[][] dir = new int[][]{{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        while (!q.isEmpty())
        {
            int[] curr = q.poll();
            for (int[] d : dir)
            {
                int i = curr[0] + d[0];
                int j = curr[1] + d[1];
                if (i < 0 || j < 0 || i >= r || j >= c || mat[i][j] <= mat[curr[0]][curr[1]] + 1)
                    continue;
                mat[i][j] = mat[curr[0]][curr[1]] + 1;
                q.offer(new int[]{i, j});
            }
        }
        return mat;
    }
}