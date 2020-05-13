
from flask_pymongo import PyMongo
mongo = PyMongo()  

myclient = PyMongo.MongoClient("mongodb://localhost:27017/")
mydb = mongo["mydatabase"]

mycol = mydb["templates"]

def create_template(c,t,d):
    mydict = { "c": "c", "t": "t", 'd':d}
    x = mycol.insert_one(mydict)