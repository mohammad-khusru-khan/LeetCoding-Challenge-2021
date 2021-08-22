/*
We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is (109)2 = (-7)2 = 49.
 

Constraints:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 109
The total area covered by all rectangles will never exceed 263 - 1 and thus will fit in a 64-bit signed integer.
*/

class Solution
{
public:
    int rectangleArea(vector<vector<int>> &rectangles)
    {
        vector<vector<int>> line;
        for (auto &rectangle : rectangles)
        {
            int x1 = rectangle[0], y1 = rectangle[1], x2 = rectangle[2], y2 = rectangle[3];
            line.push_back({y1, x1, x2, 1});
            line.push_back({y2, x1, x2, 0});
        }

        sort(line.begin(), line.end());

        long ans = 0, val = 0;
        int yy = 0, prev = 0;
        multiset<vector<int>> segments;
        for (auto &elem : line)
        {
            int y = elem[0], x1 = elem[1], x2 = elem[2], tf = elem[3];
            ans = (ans + val * (y - yy)) % 1'000'000'007;
            yy = y;
            if (tf)
                segments.insert({x1, x2});
            else
                segments.erase(segments.find({x1, x2}));
            val = prev = 0;
            for (auto &seg : segments)
            {
                x1 = seg[0];
                x2 = seg[1];
                val += max(0, x2 - max(x1, prev));
                prev = max(prev, x2);
            }
        }
        return ans;
    }
};