from neo4j.v1 import GraphDatabase, basic_auth
from flask import g, abort
from configparser import ConfigParser


config = ConfigParser()
config.read('configfile')

username = config.get('database', 'username')
password = config.get('database', 'password')
url = config.get('database', 'url')

try:
    driver = GraphDatabase.driver(url, auth=basic_auth(username, password))
except Exception as e:
    print("Exception thrown while trying to connect to neo4j database.")
    print("Are you sure it's online? Check: " + url)
    print("Raising exception:\n")
    raise e


def run(query, param={}):
    return get_db().run(query, param)

def get_db():
    global driver
    if not hasattr(g, 'neo4j_db'):
        try:
            g.neo4j_db = driver.session()
        except Exception as e:
            abort(500, "Error connecting to database")

    return g.neo4j_db
