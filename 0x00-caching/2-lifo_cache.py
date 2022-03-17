#!/usr/bin/env python3
"""Class LIFOCche that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class that inherits from BaseCaching"""

    def __init__(self):
        """init new instance var"""
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """assign to dict the item val key"""
        if (key and item):
            self.cache_data[key] = item
            if key not in self.cache_list:
                self.cache_list.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = self.cache_list.pop(self.MAX_ITEMS - 1)
                print('DISCARD: {}'.format(discarded))
                del self.cache_data[discarded]

    def get(self, key):
        """return val in self.cache_data linked to key"""
        if key or key not in self.cache_data:
            return self.cache_data.get(key)
