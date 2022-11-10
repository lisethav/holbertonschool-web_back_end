#!/usr/bin/env python3
""" Code lines """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Code lines """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
