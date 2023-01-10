from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Author(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    firstname = Column(String)
    country = Column(String)
    # book_ids = Column(Integer, ForeignKey("book.id"))
    # relationship not working for now:
    # books = relationship("Book", back_populates="author")
