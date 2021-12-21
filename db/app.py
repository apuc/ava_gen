from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
load_dotenv()
mysql_conf = os.getenv('MYSQL')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = mysql_conf
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Figure(db.Model):
    __tablename__ = 'figure'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    type_id = db.Column(db.Integer(), db.ForeignKey("type.id"), nullable=False)
    label = db.Column(db.String(255, collation="utf8mb4_unicode_ci"))
    age = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.Integer, nullable=True, default=0)
    rnd_fill = db.Column(db.Integer, nullable=True)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Ava(db.Model):
    __tablename__ = 'ava'
    id = db.Column(db.String(255, collation="utf8mb4_unicode_ci"), primary_key=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.Integer, nullable=True)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Ava_figure(db.Model):
    __tablename__ = 'ava_figure'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    ava_id = db.Column(db.String(255, collation="utf8mb4_unicode_ci"), db.ForeignKey("ava.id"), nullable=False)
    figure_id = db.Column(db.Integer(), db.ForeignKey("figure.id"), nullable=False)
    fill = db.Column(db.String(255, collation="utf8mb4_unicode_ci"), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Fill(db.Model):
    __tablename__ = 'fill'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    value = db.Column(db.String(255, collation="utf8mb4_unicode_ci"), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Path(db.Model):
    __tablename__ = 'path'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    d = db.Column(db.TEXT(collation="utf8mb4_unicode_ci"), nullable=False)
    extend_fill = db.Column(db.Integer, nullable=True)
    figure_id = db.Column(db.Integer(), db.ForeignKey("figure.id"), nullable=False)
    fill_id = db.Column(db.Integer(), db.ForeignKey("fill.id"), nullable=False)
    priority = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=True)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Figure %r>' % self.id


class Type(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(255, collation="utf8mb4_unicode_ci"), nullable=False)
    slug = db.Column(db.String(255, collation="utf8mb4_unicode_ci"), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Type %r>' % self.id

    @staticmethod
    def get_query_fields():
        return {'id': '#', 'slug': 'Slug', 'label': 'Label'}



class Type_Fill(db.Model):
    __tablename__ = 'type_fill'
    id = db.Column(db.Integer, primary_key=True)
    fill_id = db.Column(db.Integer(), db.ForeignKey("fill.id"), nullable=False)
    type_id = db.Column(db.Integer(), db.ForeignKey("type.id"), nullable=False)

    def __init__(self):
        pass



if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
