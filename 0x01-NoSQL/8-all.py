#!/usr/bin/env python3
"""
Module with function that lists all
documents in a collection
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    returns:
      empty list if no document is in the collection
    """
    return [doc for doc in mongo_collection.find()]
