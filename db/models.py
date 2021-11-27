from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TEXT
from db.base import Base


class Crud:
    total = 0

    def __init__(self, model: Base):
        self.model = model
        self.total = 0

    def pagination(self, page: int, per_page: int):
        pass

    def get_total(self):
        return self.model.query.count()


class Figure(Base):
    __tablename__ = 'figure'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    type = Column(Integer, nullable=False)
    age = Column(Integer, nullable=True)
    sex = Column(Integer, nullable=True, default=0)
    rnd_fill = Column(Integer, nullable=True)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Ava(Base):
    __tablename__ = 'ava'
    id = Column(String(255, collation="utf8mb4_unicode_ci"), primary_key=True, nullable=False)
    age = Column(Integer, nullable=True)
    sex = Column(Integer, nullable=True)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Ava_figure(Base):
    __tablename__ = 'ava_figure'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ava_id = Column(String(255, collation="utf8mb4_unicode_ci"), ForeignKey("ava.id"), nullable=False)
    figure_id = Column(Integer(), ForeignKey("figure.id"), nullable=False)
    fill = Column(String(255, collation="utf8mb4_unicode_ci"), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Fill(Base):
    __tablename__ = 'fill'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    value = Column(String(255, collation="utf8mb4_unicode_ci"), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Path(Base):
    __tablename__ = 'path'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    d = Column(TEXT(collation="utf8mb4_unicode_ci"), nullable=False)
    extend_fill = Column(Integer, nullable=True)
    figure_id = Column(Integer(), ForeignKey("figure.id"), nullable=False)
    fill = Column(String(255, collation="utf8mb4_unicode_ci"), nullable=False)
    priority = Column(Integer, nullable=True)
    status = Column(Integer, nullable=True)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Type(Base, Crud):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    label = Column(String(255, collation="utf8mb4_unicode_ci"), nullable=False)
    slug = Column(String(255, collation="utf8mb4_unicode_ci"), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id
