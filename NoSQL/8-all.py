#!/usr/bin/env Python3
"""List all the documents in the collection"""


def list_all(mongo_collection):
    """List all documents in Python"""
    if not mongo_collection:
        return []
    return mongo_collection.find()
