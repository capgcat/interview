from fastapi import FastAPI, Request
import os
import requests
from mongo import MongoConnection

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb+srv://karthikkumarkrishnamoorthy:3oMcG5oBZuzoYJJ6@cluster0.sdyfthn.mongodb.net")  # Replace with your actual MongoDB URL

class DatabaseService:
    def __init__(self) -> None:
        self._db = None
        self._provider = None

        connection_params = {
            'connected_on': "mongo_cluster"
        }

        connection_params['mongodb_uri'] = MONGODB_URL
        self._provider = MongoConnection(connection_params)
    
    def close_connection(self):
        return self._provider.close_conn()
    
    def get_collection(self, collection_name: str, db_name: str = None):
        if db_name is None:
            collection = self.collections.get(collection_name)
            if collection is None:
                raise KeyError(f"{collection_name} is not a valid collection name")
            return collection
        else:
            db = self.client[db_name]
            return db[collection_name]
    
    @property
    def client(self):
        return self._provider.client
    
    @property
    def db(self):
        if self._db:
            return self._provider.client[self._db]
        return self._provider.db
    
    def set_client_db(self, database_name):
        if database_name:
            self._db = database_name
