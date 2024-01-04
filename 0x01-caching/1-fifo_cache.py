#!/usr/bin/env python3
"""
FIFO
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Caching system
    """
    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        assign to the dict self.cache_data the item value for key
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item


    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
