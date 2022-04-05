class LRUCache:

    def __init__(self, capacity: int):
        
        self.LRU = collections.OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.LRU:
            self.LRU.move_to_end(key)
            return self.LRU[key]
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        
        if key not in self.LRU and len(self.LRU) >= self.capacity:
            self.LRU.popitem(last=False)
        
        self.LRU[key] = value
        self.LRU.move_to_end(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)