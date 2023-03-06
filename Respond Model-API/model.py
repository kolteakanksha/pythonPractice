from sqlalchemy import String, Integer, Column, Boolean
from database import base, engine


class person(base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    fname = Column(String(40), nullable=False)
    lname = Column(String(40), nullable=False)
    ismale = Column(Boolean)


def create_tables():
    base.metadata.create_all(engine)
