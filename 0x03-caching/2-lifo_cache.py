#!/usr/bin/python3
"""2. LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching
     and is a caching system
    """

    def __init__(self):
        """Initialiaze the class"""
        
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data
         the item value for the key """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            disca = self.__keys.pop()
            del self.cache_data[disca]
            print('DISCARD: {}'.format(disca))
        if key and item:
            self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
