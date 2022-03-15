#!/usr/bin/env python3
""" 11-schhols_by_topic.py """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """Func that returns list of schools having specific topic"""
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.find({'topics': topic})
