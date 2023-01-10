from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Stock(Base):
    id = Column(Integer, primary_key=True, index=True)
    qty_on_hand = Column(String)
    qty_total = Column(String)
