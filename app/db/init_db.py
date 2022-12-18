# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from db.session import engine
# from db.base_class import Base

# # init_DB
# # Base class used by my classes (my entities)
# Base = declarative_base()    # Required
# Base.metadata.create_all(bind=engine)

from sqlalchemy.orm import Session
from db.base import Base

def init_db(db: Session) -> None:

    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)
