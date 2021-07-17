import lru_cache

d=lru_cache.LRU(3)

d.put(2,5)
d.put(5,"saimanish")
d.put(3,9)
print(d.get_cache())
print(d.get(5))
d.put(5,7)
d.put(2,0)
print(d.get_cache())