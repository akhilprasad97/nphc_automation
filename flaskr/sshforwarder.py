import os
import sys


import json
import pymongo

from sshtunnel import SSHTunnelForwarder
import pprint


hostname = "10.127.250.99"
username = "calo"
password = "cisco"
#MONGO_DB = "temp_UI"

server = SSHTunnelForwarder(
hostname,
ssh_username=username,
ssh_password=password,
remote_bind_address=('127.0.0.1', 27017)
)

server.start()

client = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
db = client["temp_ASR9K"]
pprint.pprint(db.collection_names())



    

