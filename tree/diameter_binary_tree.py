from typing import Optional
from util.tree_node import TreeNode

# https://leetcode.com/problems/diameter-of-binary-tree/

"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node: Optional[TreeNode], height: int) -> None:
            nonlocal diameter
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            diameter = max(diameter, l + r)
            return 1 + max(l, r)

        dfs(root, 0)
        return diameter
