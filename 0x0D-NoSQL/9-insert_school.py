#!/usr/bin/env python3
""" Code lines """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Code lines """
    return mongo_collection.insert_one(kwargs).inserted_id
