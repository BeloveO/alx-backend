#!/usr/bin/python3
"""
FIFO
"""


from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    Caching system
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
        self.cache_data[key] = item
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
