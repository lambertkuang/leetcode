from typing import Optional

"""
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
"""

class ListNode:
    def __init__(self, key: int, value: int, prev: Optional['ListNode'] = None, next: Optional['ListNode'] = None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.store = {}
        self.lru_head = None
        self.lru_tail = None

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]
        self.remove(key)
        self.insert(key, node.value)
        return node.value

    def remove(self, key: int) -> None:
        if key not in self.store:
            return
        if key == self.lru_head.key:
            self.lru_head = self.lru_head.next
            if self.lru_head:
                self.lru_head.prev = None
        if key == self.lru_tail.key:
            if self.lru_tail.prev:
                self.lru_tail.prev.next = None
                self.lru_tail = self.lru_tail.prev
        else:
            node = self.store[key]
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

        del self.store[key]
        self.size -= 1

    def insert(self, key: int, value: int) -> None:
        node = ListNode(key, value)
        if not self.lru_head:
            self.lru_head = node
        if not self.lru_tail:
            self.lru_tail = node
        else:
            node.prev = self.lru_tail
            self.lru_tail.next = node
            self.lru_tail = node
        self.store[key] = node
        self.size += 1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(key)
            self.insert(key, value)
            return

        if self.size == self.capacity:
            self.remove(self.lru_head.key)
        self.insert(key, value)
