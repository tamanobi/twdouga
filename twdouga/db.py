import os
import databases
import sqlalchemy

DATABASE_URL = os.environ['DATABASE_URL']
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

ECHO_LOG = False

database = databases.Database(DATABASE_URL, min_size=5, max_size=20)
engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)
metadata = sqlalchemy.MetaData()
