#!/usr/bin/env python3
"""
BaseCaching module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system
    """
    def put(self, key, item):
        """
        assign to the dict self.cache_data the item value for key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
