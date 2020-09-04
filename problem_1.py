from collections import OrderedDict
class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1
        
    def set(self, key, value):
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        if key not in self.cache:
            self.cache[key] = value
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value

    def print_cache(self):
        print(self.cache)
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(2, 2.1) #testing case where item in cache gets overwritten
our_cache.set(4, 4)
our_cache.print_cache()

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))     # returns 2.1
print(our_cache.get(9))     #testing case where item is not in cache; returns -1

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))    #testing case where previously stored item no longer present due to exceeded capacity; returns -1
our_cache.print_cache()
print(our_cache.get(4))  
