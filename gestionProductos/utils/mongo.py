from urllib import response
from pymongo import MongoClient
from django.conf import settings

class MongoConnection():
    def __init__(self):
        self.client = MongoClient(settings.MONGO_HOST, 
                                  username = settings.MONGO_USERNAME,
                                  password = settings.MONGO_PASSWORD,
                                  authMechanism = 'SCRAM-SHA-256')

    def get_databases(self):
        print(self.client.list_database_names())

    def insert_document(self, documento):
        db = self.client.test_example_db
        collection = db.users
        collection.insert_one(documento)
    
    def find_all_documents(self):
        db = self.client.test_example_db
        collection = db.users
        response = collection.find({})
        
        return response

    def find_specific_documents(self, condicion):
        db = self.client.test_example_db
        collection = db.users
        response = collection.find(condicion)
        
        return response
    
    def delete_documents(self, condicion):
        db = self.client.test_example_db
        collection = db.users
        collection.find_one_and_delete(condicion)
        