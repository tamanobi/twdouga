from twdouga.db import engine
from twdouga.models import *
from sqlalchemy.orm import sessionmaker


def init_db():
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(bind=engine)
    session.flush()