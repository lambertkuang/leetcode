from collections import deque
from typing import Optional

from util.tree_node import TreeNode

# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        results = []
        q = deque()
        if root:
            q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            results.append(level)

        return results