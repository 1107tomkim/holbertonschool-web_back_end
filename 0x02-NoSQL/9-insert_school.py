#!/usr/bin/env python3
""" 9-insert_school.py """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Inserts new doc in collection based kwargs"""
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.insert_one(kwargs).inserted_id
