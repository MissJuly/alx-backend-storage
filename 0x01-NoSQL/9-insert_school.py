#!/usr/bin/env python3
"""
Module with function that inserts a new document in
collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in a collection
    returns:
        the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
