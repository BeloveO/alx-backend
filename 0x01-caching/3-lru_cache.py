#!/usr/bin/env python3
"""
Least recently used caching module
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Least recently used Caching system
    """
    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assign to the dict self.cache_data the item value for key
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
