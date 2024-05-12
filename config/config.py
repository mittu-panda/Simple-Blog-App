
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mittupanda590:Mittu1234@mittu.s7psvhr.mongodb.net/?retryWrites=true&w=majority&appName=Mittu"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Blogging
blogs_collection = db["blogs"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)