from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TEXT
from db.base import Base


class Crud:
    total = 0

    def __init__(self, model: Base):
        self.model = model
        self.total = self.model.query.count()
        self.page_count = None
        self.items = None
        self.current_page = None
        self.request_dict = {}

        self.query = self.model.query

    def set_query(self, q):
        for key in q:
            col = getattr(self.model, key)
            self.query = self.query.filter(col.contains(q[key]))

    def prepare_request(self, request):
        for field in self.model.get_query_fields():
            if field in request.args:
                self.request_dict[field] = request.args.get(field)

    def request(self, request, per_page=5):
        self.prepare_request(request)
        self.set_query(self.request_dict)
        self.pagination(int(request.args.get('page', 1)), per_page)

    def pagination(self, page: int, per_page: int):
        self.current_page = page
        offset = (page - 1) * per_page
        self.page_count = self.total // per_page
        if (self.total % per_page) >= 1:
            self.page_count += 1
        self.items = self.query.limit(per_page).offset(offset).all()

    def get_total(self):
        return self.total


class Figure(Base):
    __tablename__ = 'figure'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    type_id = Column(Integer(), ForeignKey("type.id"), nullable=False)
    label = Column(String(255, collation="utf8mb4_unicode_ci"))
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
    fill_id = Column(Integer(), ForeignKey("fill.id"), nullable=False)
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
        return '<Type %r>' % self.id

    @staticmethod
    def get_query_fields():
        return ['id', 'slug', 'label']

