#!/usr/bin env python3
""" 10-update_topics.py """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Func that changes topics of school doc based on name"""
    return mongo_collection.update_many({"name": name}, { "$set": { "topics": topics } })
