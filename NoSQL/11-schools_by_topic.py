#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Return the list of school having a specific topic"""
    if not mongo_collection:
        return []
    return mongo_collection.find({"topics": topic})
