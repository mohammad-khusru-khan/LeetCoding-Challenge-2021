/*
You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.

 

Example 1:


Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
Example 2:


Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]
 

Constraints:

1 <= points.length <= 3000
points[i].length == 2
0 <= xi, yi <= 100
All the given points are unique.
*/

int start_x_new = 0;
int start_y_new = 0;
void calling(int a, int b)
{
    start_x_new = a;
    start_y_new = b;
}
class Solution
{
    int check_determinant(pair<int, int> p, pair<int, int> v, pair<int, int> c)
    {
        int x1 = v.first - p.first;
        int y1 = v.second - p.second;
        int x2 = c.first - v.first;
        int y2 = c.second - v.second;
        return y2 * x1 - y1 * x2;
    }
    static bool again(const vector<int> &a, const vector<int> &b)
    {
        return a[1] < b[1];
    }
    static bool compare(const vector<int> &a, const vector<int> &b)
    {
        double y1 = (a[1] - start_y_new);
        double x1 = (a[0] - start_x_new);
        double angle1 = atan(y1 / x1) * (180.00 / M_PI);
        if (angle1 < 0.00)
            angle1 = 90.000 + abs(angle1);
        double y2 = (b[1] - start_y_new);
        double x2 = (b[0] - start_x_new);
        double angle2 = atan(y2 / x2) * (180.00 / M_PI);
        if (angle2 < 0.00)
            angle2 = 90.000 + abs(angle2);
        if (angle1 == angle2)
        {
            if (a[0] != b[0])
                return a[0] < b[0];
            else
                return a[1] > b[1];
        }
        if (angle1 > 90.000 && angle2 > 90.000)
            return angle1 > angle2;
        return angle1 < angle2;
    }

public:
    vector<vector<int>> outerTrees(vector<vector<int>> &trees)
    {
        if (trees.size() == 1)
            return trees;
        int start_x = 0, start_y = 0;
        int mini_y = INT_MAX;
        int index = 0;
        for (int i = 0; i < trees.size(); i++)
            if (trees[i][1] < mini_y)
            {
                start_x = trees[i][0];
                start_y = trees[i][1];
                mini_y = trees[i][1];
                index = i;
            }
        calling(start_x, start_y);
        trees.erase(trees.begin() + index);
        sort(trees.begin(), trees.end(), compare);
        int u = 0;
        while (u < trees.size() && trees[u][0] == start_x_new)
            u++;
        sort(trees.begin(), trees.begin() + u, again);
        stack<pair<int, int>> st;
        st.push({start_x_new, start_y_new});
        pair<int, int> p = st.top();
        st.push({trees[0][0], trees[0][1]});
        pair<int, int> v = st.top();
        int i = 1;
        while (i < trees.size() && !st.empty())
        {
            pair<int, int> c = {trees[i][0], trees[i][1]};
            if (check_determinant(p, v, c) >= 0)
            {
                st.push(c);
                p = v;
                v = c;
                i++;
            }
            else
            {
                st.pop();
                v = st.top();
                st.pop();
                p = st.top();
                st.push(v);
            }
        }
        vector<vector<int>> ans;
        while (!st.empty())
        {
            vector<int> y;
            y.push_back(st.top().first);
            y.push_back(st.top().second);
            st.pop();
            ans.push_back(y);
        }
        return ans;
    }
};