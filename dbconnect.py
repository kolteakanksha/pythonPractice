
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Column, Boolean, Float, DateTime
import pandas as pd

engine = create_engine("postgresql://postgres:root@localhost/chunkuploads", echo=True)
base = declarative_base()


class Chunk(base):
    __tablename__ = 'Chunks'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True)
    duration = Column(Integer)
    pulse = Column(Integer)
    maxpulse = Column(Integer)
    calories = Column(Float)


#base.metadata.create_all(engine)

file_name = r"C:\Users\pnema\OneDrive\Desktop\data.csv"
df = pd.read_csv(file_name)
df.to_sql(con=engine, name=Chunk.__tablename__, index=False, chunksize=100)

#session = sessionmaker()
#session.configure(bind=engine)
#s = session()
#s.query(Chunk).all()
