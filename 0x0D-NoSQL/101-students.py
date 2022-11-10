#!/usr/bin/env python3
""" Code lines """
import pymongo


def top_students(mongo_collection):
    """ Code lines """
    return mongo_collection.aggregate([
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
