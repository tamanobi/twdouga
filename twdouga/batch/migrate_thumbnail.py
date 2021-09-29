from twdouga.db import engine
from twdouga.models import Request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc, and_, or_

session = sessionmaker(bind=engine)()
# requests = session.query(Request).filter(and_(Request.thumbnail_url == "", Request.response is None))
requests = session.query(Request).filter(or_(Request.thumbnail_url == None, Request.thumbnail_url == "")).all()
for r in requests:
    if r.response is None:
        continue
    media = r.response.get("extended_entities", {}).get("media", [{}])[0]
    thumbnail_url = media.get("media_url_https", "")
    r.thumbnail_url = thumbnail_url
session.commit()
