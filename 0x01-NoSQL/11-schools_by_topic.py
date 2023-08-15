#!/usr/bin/env python3
"""
Module with function that returns the list
of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school
    """
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
