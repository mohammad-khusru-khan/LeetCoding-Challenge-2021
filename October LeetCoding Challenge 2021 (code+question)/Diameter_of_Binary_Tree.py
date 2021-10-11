'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_L, other_L = self.helper(root)
        return max(max_L, other_L) - 1

    def helper(self, root):
        if not root:
            return 0, 0
        left_path, max_in_left = self.helper(root.left)
        right_path, max_in_right = self.helper(root.right)
        left_and_right_path = left_path + right_path + 1

        max_path_one = max(left_path, right_path) + 1
        max_all = max(left_and_right_path, max_in_left, max_in_right)

        return max_path_one, max_all
