class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.nxt = self.prv = None 
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map key to nodes

        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.nxt = self.right
        self.right.prv = self.left

    def insert(self, node):
        prv, nxt = self.right.prv, self.right

        prv.nxt = nxt.prv = node
        node.nxt, node.prv = nxt, prv
        
    def remove(self, node):
        prev = node.prv
        nxt = node.nxt
        prev.nxt, nxt.prv = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]

        
