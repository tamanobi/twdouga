from sqlalchemy import func
from sqlalchemy.schema import Column, Index
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Request(Base):
    """ダウンロードリクエスト"""

    __tablename__ = "request"

    id = Column(Integer, primary_key=True)
    status = Column(String(length=32), nullable=False)
    video_url = Column(String(length=128), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = (Index('created_at__status', "created_at", "status"), )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# class TwitterStatus(Base):
#     """Twitter Status"""

#     __tablename__ = "twitter_status"

#     status = Column(String(length=32), primary_key=True)
#     count = Column(Integer, default=1, nullable=False)
#     updated_at = Column(DateTime, nullable=False, onupdate=func.now())
#     created_at = Column(DateTime, nullable=False, server_default=func.now())
