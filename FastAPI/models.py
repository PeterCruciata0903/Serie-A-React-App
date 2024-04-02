from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    position = Column(String)
    nationality = Column(String)
    team = Column(String)
    value = Column(Float)