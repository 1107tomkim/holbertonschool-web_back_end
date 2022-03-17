#!/usr/bin/env python3
"""Class MRUCache that inherits from BaseCaching"""
from typing import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class that inherits from BaseCaching"""

    def __init__(self):
        """init instance var"""
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to dict the item val for key"""
        if (key and item):
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                cache_list = list(self.cache_data.keys())
                discard = cache_list[self.MAX_ITEMS - 1]
                print('DISCARD: {}'.format(discard))
                del self.cache_data[discard]

    def get(self, key):
        """retuns the val in self.cache_data linked to key"""
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
