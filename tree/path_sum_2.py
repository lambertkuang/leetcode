from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        paths = []

        def dfs(node: Optional[TreeNode], cur_path: list, cur_sum: int) -> None:
            if not node:
                return

            cur_sum += node.val
            cur_path.append(node.val)

            if cur_sum == targetSum and not node.left and not node.right:
                paths.append(cur_path.copy())

            dfs(node.left, cur_path.copy(), cur_sum)
            dfs(node.right, cur_path.copy(), cur_sum)

        dfs(root, [], 0)

        return paths
