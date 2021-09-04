/*
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]
 

Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
*/

class Solution
{
    vector<vector<int>> adj;
    vector<int> ans;
    vector<bool> vis;
    vector<int> numNodes;
    int n;

    pair<int, int> dfs1(int u)
    {
        vis[u] = true;

        pair<int, int> ret = make_pair(0, 1);
        for (int v : adj[u])
        {
            if (!vis[v])
            {
                auto [sumDist, numOfNodes] = dfs1(v);
                ret.first += (sumDist + numOfNodes);
                ret.second += numOfNodes;
            }
        }

        numNodes[u] = ret.second;
        return ret;
    }

    void dfs2(int u, int sumParent)
    {
        vis[u] = true;

        if (u != 0)
            ans[u] = sumParent - numNodes[u] + (n - numNodes[u]);
        else
            ans[u] = sumParent;
        for (int v : adj[u])
        {
            if (!vis[v])
                dfs2(v, ans[u]);
        }
    }

public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>> &edges)
    {
        adj.resize(n, vector<int>());
        this->n = n;
        for (auto v : edges)
        {
            adj[v[0]].push_back(v[1]);
            adj[v[1]].push_back(v[0]);
        }

        vis.resize(n, false);
        numNodes.resize(n, -1);
        auto [sumDist, numOfNodes] = dfs1(0);
        ans.resize(n, -1);
        vis.clear();
        vis.resize(n, false);
        dfs2(0, sumDist);
        return ans;
    }
};