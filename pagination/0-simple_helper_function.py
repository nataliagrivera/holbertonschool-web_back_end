#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size two containing a start index and na end index"""
    return ((page - 1) * page_size, page * page_size)
