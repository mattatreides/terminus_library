from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    # author_id = Column(Integer, ForeignKey("author.id"))
    # author = relationship("Author", back_populates="name")

    def __init__(self, pk=0, tt="John", des="Doe"):
        self.id = pk
        self.title = tt
        self.description = des