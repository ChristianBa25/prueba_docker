from pymongo import MongoClient
from django.conf import settings

class MongoConnection():
    def __init__(self):
        self.client = MongoClient(settings.MONGO_HOST, username=settings.MONGO_USERNAME, password=settings.MONGO_PASSWORD, authMechanism='SCRAM-SHA-256')
    
    def get_databases(self):
        print(self.client.list_database_names())
        
    def insert_document(self, name, lastname, age, email):
        db = self.client.test_example_db
        collection = db.users
        response = collection.insert_one({'name': name, 'lastname': lastname, 'age': age, 'email': email})
        
    def find_document(self, name):
        db = self.client.test_example_db
        collection = db.users
        response = collection.find({'age': {'$gt': 20}})
        return response
        