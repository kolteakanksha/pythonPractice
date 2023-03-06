from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:root@localhost/person", echo=True)
base = declarative_base()
sessionlocal = sessionmaker(bind=engine)

print(dir())#
