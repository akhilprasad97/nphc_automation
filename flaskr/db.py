

import pymongo

from sshtunnel import SSHTunnelForwarder
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_mongo():
    if 'mongo' not in g:
        hostname = "10.127.250.99"
        username = "calo"
        password = "cisco"
        
        server = SSHTunnelForwarder(
        hostname,
        ssh_username=username,
        ssh_password=password,
        remote_bind_address=('127.0.0.1', 27017)
        )

        server.start()
        g.mongo = pymongo.MongoClient('127.0.0.1', server.local_bind_port)

    return g.mongo



def close_mongo(e=None):
    mongo = g.pop('mongo', None)

    if mongo is not None:
        mongo.close()

def init_app(app):
    app.teardown_appcontext(close_mongo)

