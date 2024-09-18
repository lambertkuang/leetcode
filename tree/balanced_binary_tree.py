from typing import Optional
from util.tree_node import TreeNode

"""
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true


Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false


Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height balanced means the difference in height between the left
        # and right subtrees is less than or equal to one
        is_balanced = True
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal is_balanced
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if abs(left_height - right_height) > 1:
                is_balanced = False
            return 1 + max(left_height, right_height)

        dfs(root)

        return is_balanced