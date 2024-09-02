from collections import deque
from typing import Optional

from util.tree_node import TreeNode


class CodecBFS:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoded = ''
        queue = deque()
        queue.append(root)

        while queue and not all(i is None for i in queue):
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if node is None:
                    encoded += 'None'
                    queue.append(None)
                    queue.append(None)
                else:
                    encoded += str(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                encoded += ' '
        return encoded

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        root = None
        d = data.split()
        for i in range(len(d)):
            cur = d[i]
            if cur == 'None':
                continue

            parent_idx = (i - 1) // 2
            if parent_idx >= 0:
                node = cur
            else:
                root = TreeNode(int(cur))
                node = root
                d[i] = node
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(d):
                left = d[left_idx]
                if left != 'None':
                    node.left = TreeNode(int(left))
                    d[left_idx] = node.left

            if right_idx < len(d):
                right = d[right_idx]
                if right != 'None':
                    node.right = TreeNode(int(right))
                    d[right_idx] = node.right

        return root



node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(4)
node.left.right = TreeNode(1)


serialized = CodecBFS().serialize(node)
# print(serialized)
print(CodecBFS().deserialize('1 2 3 None None 4 5 6 7'))


class CodecDFS:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                res.append('N')
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        data = data.split(',')
        def dfs() -> TreeNode:
            val = data[self.i]
            if val == 'N':
                self.i += 1
                return None
            node = TreeNode(int(val))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()



print(CodecDFS().deserialize('5,3,N,1,N,N,4,N,N'))