#!/usr/bin/env python3
"""Log stats"""


from pymongo import MongoClient

def get_logs_count():
    with MongoClient('mongodb://127.0.0.1:27017') as client:
        col = client.logs.nginx
        return col.count_documents({})

def get_method_count(method):
    with MongoClient('mongodb://127.0.0.1:27017') as client:
        col = client.logs.nginx
        return col.count_documents({'method': method})

def get_status_check_count():
    with MongoClient('mongodb://127.0.0.1:27017') as client:
        col = client.logs.nginx
        return col.count_documents({'method': 'GET', 'path': '/status'})

def main():
    logs_count = get_logs_count()
    print(f"{logs_count} logs")

    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = get_method_count(method)
        print(f"\tmethod {method}: {count}")

    status_check_count = get_status_check_count()
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    main()
