#!/usr/bin env python3
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Func that changes topics of school doc based on name"""
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
        )
