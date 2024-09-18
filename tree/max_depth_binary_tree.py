from typing import Optional
from util.tree_node import TreeNode


"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3


Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(node: Optional[TreeNode], depth: int = 1) -> None:
            nonlocal max_depth
            if not node:
                return

            max_depth = max(max_depth, depth)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root)

        return max_depth