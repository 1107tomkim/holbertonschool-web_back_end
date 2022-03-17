#!/usr/bin/env python3
"""Creates class LRUCache that inherits from BaseCaching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Class that inherits from BaseCaching"""

    def __init__(self):
        """init new instance var"""
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to dict the item val for key"""
        if (key and item):
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        if (len(self.cache_data) > self.MAX_ITEMS):
            discard = self.cache_data.popitem(last=False)
            print('DISCARD: {}'.format(discard[0]))

    def get(self, key):
        """return val in self.cache_data linked to key"""
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
