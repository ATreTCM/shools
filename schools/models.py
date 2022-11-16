
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship, declarative_base


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
    hall_id = Column(Integer(), ForeignKey("Hall.id")
    coach_id = Column(Integer(), ForeignKey("User.id")
    hall = relationship(
        Hall, backref=backref("halls", uselist=True, cascade="delete,all")
    )
    coach = relationship(
        User, backref=backref("coachs", uselist=True, cascade="delete,all")
    )
