from util.node import Node
from util.test_case import TestCase


from typing import Optional
class Solution(TestCase):
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        # store newly created nodes
        self.store: dict[int, Node] = {}
        self.clone(node)
        return self.store[node.val]

    def clone(self, node: Node) -> None:
        if node.val not in self.store:
            self.store[node.val] = Node(node.val)

        for neighbor in node.neighbors:
            if neighbor.val not in self.store:
                self.clone(neighbor)
            self.store[node.val].neighbors.append(self.store[neighbor.val])

    def method(self):
        return self.cloneGraph
