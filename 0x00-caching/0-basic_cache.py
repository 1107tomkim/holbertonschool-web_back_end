#!/usr/bin/env python3
"""Creates a class that inherits from BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class that inherits from BaseCaching"""

    def put(self, key, item):
        """Assign dict to the item val"""
        if (key and item):
            self.cache_data[key] = item

    def get(self, key):
        """Returns val in linked key"""
        if key:
            return self.cache_data.get(key)
