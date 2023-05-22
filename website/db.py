'''
Imports
'''
import os
from pymongo import MongoClient
from dotenv import load_dotenv

def get_collection(collection: str) -> object:
    '''
    Return collection from SchoolData databse
    '''

    load_dotenv()

    uri = os.getenv("MONGODB_URI")

    client = MongoClient(uri)

    database = client.SchoolData

    return database[collection].find()
