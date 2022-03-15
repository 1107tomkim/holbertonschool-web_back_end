#!/usr/bin/env python3
from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all doc in a collection"""
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.find()
