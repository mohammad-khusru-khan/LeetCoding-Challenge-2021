'''
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def bfs(node, target):
            q = deque()
            q.append((node, 0, None))
            while q:
                curr_node, dist, parent = q.popleft()
                if curr_node.val == target:
                    return dist, parent
                if curr_node.left:
                    q.append((curr_node.left, dist + 1, curr_node))
                if curr_node.right:
                    q.append((curr_node.right, dist + 1, curr_node))
            return None

        bfs_x = bfs(root, x)
        bfs_y = bfs(root, y)
        if bfs_x is None or bfs_y is None:
            return False
        dist_x, parent_x = bfs_x[0], bfs_x[1]
        dist_y, parent_y = bfs_y[0], bfs_y[1]
        if dist_x == dist_y and parent_x != parent_y:
            return True
        return False