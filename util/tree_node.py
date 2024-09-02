from collections import deque
from typing import Any, Optional


class TreeNode:
    def __init__(self, val: Any, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def print(self) -> None:
        queue = deque()
        queue.append(self)

        while queue:
            cur_level = ''
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    cur_level += 'None '
                    continue
                cur_level += str(node.val) + ' '
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(cur_level)

