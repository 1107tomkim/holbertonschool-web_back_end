#!/usr/bin/env python3
"""Class FIFOCache that inherits from BaseCaching"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class that inherits from BaseCaching"""

    def __init__(self):
        """init new instance var"""
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assignt to dict the item val for the key"""
        if (key and item):
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                k, v = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(k))

    def get(self, key):
        """return val in self.cache_data linked to key"""
        if key or key not in self.cache_data:
            return self.cache_data.get(key)
