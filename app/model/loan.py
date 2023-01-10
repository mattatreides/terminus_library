from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

from app.db.base_class import Base

class Loan(Base):
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("book.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    date_start = Column( DateTime)
    date_return_exp = Column( DateTime)
    date_end = Column( DateTime)