#!/usr/bin/env python3
""" Code lines """
import pymongo


def list_all(mongo_collection):
    """ Code lines """
    return [p for p in mongo_collection.find()] if mongo_collection else []
