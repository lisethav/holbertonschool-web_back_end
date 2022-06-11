#!/usr/bin/env python3
"""3. LRU Caching"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """class LRUCache that inherits from BaseCaching
     and is a caching system"""

    def __init__(self) -> None:
        """Initialiaze the class"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
         the item value for the key key"""
        if (key is not None) and (item is not None):
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                keys = next(iter(self.cache_data))
                del self.cache_data[keys]
                print("DISCARD: {}".format(keys))

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if (key is None) or (key not in self.cache_data):
            return None
        value = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = value
        return value
