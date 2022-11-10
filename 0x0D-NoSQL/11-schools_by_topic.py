#!/usr/bin/env python3
""" Code lines """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Code lines """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
