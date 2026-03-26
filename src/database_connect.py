import os
from pymongo import MongoClient
from pandas import DataFrame

class mongo_operation:
    def __init__(self, client_url: str, database_name: str):
        self.client = MongoClient(client_url)
        self.db = self.client[database_name]

    def bulk_insert(self, data, collection_name: str):
        if isinstance(data, DataFrame):
            records = data.to_dict("records")
        else:
            records = list(data)
        if not records:
            return
        self.db[collection_name].insert_many(records)

    def find(self, collection_name: str):
        docs = list(self.db[collection_name].find({}))
        for d in docs:
            d.pop("_id", None)
        return docs