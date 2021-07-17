from collections import OrderedDict

class LRU:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity