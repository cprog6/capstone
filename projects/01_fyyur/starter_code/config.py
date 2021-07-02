import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# TODO: connect to a local postgresql database

DEBUG = True

DB_CONFIG = {
        'host':  'localhost',
        'dbname': 'rickdb',
        'user': 'postgres',
        'password': 'Theoilers1#'
}

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Theoilers1#@localhost:5432/rickdb"
