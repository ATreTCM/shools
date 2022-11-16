
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

__all__ = ('Hall', 'User', 'Lesson', )


class Hall(Base):
    __tablename__ = "hall"

    id = Column(Integer(), primary_key=True)
    city = Column(String(20), nullable=False)
    street = Column(String(40), nullable=False)


    
class User(Base):
    __tablename__ = "user"

    id = Column(Integer(), primary_key=True)
    name = Column(String(40), nullable=False)
   


class Lesson(Base):
    __tablename__ = "lesson"
    
    id = Column(Integer, primary_key=True)
    hall_id = Column(Integer(), ForeignKey("Hall.id", ondelete="CASCADE"))
    coach_id = Column(Integer(), ForeignKey("User.id", ondelete="CASCADE"))




