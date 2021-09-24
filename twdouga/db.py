import os
import databases
import sqlalchemy

DATABASE_URL = os.environ['DATABASE_URL']
ECHO_LOG = False

database = databases.Database(DATABASE_URL, min_size=5, max_size=20)
engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)
metadata = sqlalchemy.MetaData()
