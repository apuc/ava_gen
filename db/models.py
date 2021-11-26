from sqlalchemy import Column, Integer, String
from db.base import Base


class Figure(Base):
    __tablename__ = 'figure'
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    age = Column(Integer)
    sex = Column(Integer)
    rnd_fill = Column(Integer)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id
