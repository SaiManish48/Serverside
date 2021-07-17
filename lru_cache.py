from collections import OrderedDict

class LRU:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get_cache(self):
        return self.cache
    
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    # [(3,6),(4,3)]
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
