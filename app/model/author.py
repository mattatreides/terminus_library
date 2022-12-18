from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Author(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    firstname = Column(String)
    country = Column(String)
    author_id = Column(Integer, ForeignKey("book.id"))
    author = relationship("Book", back_populates="Author")
