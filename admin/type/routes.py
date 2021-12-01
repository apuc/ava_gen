from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.base import Base, db_session
from db.models import Type, Crud
from sqlalchemy import select, func, Integer, Table, Column, MetaData

type_page = Blueprint('type', __name__, template_folder='templates')


@type_page.route('/type', defaults={'current_page': 1})
@type_page.route('/type/<current_page>')
def index(current_page):
    crud = Crud(Type)
    crud.pagination(int(request.args.get('page', 1)), 2)
    return render_template('admin/type/index.html', crud=crud)


@type_page.route('/type/create', methods=['GET'])
def create():
    type_model = Type()
    return render_template('admin/type/form.html', type_model=type_model)


@type_page.route('/type/remove/<id>')
def remove(id):
    type_model = Type.query.filter_by(id=id).first()
    db_session.delete(type_model)
    db_session.commit()

    flash('Запись удалена')
    return redirect(url_for('type.index'))


@type_page.route('/type/edit/<id>')
def edit(id):
    type_model = Type.query.filter_by(id=id).first()

    return render_template('admin/type/form.html', type_model=type_model)


@type_page.route('/type/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    if id == 'None':
        type_model = Type()
    else:
        type_model = Type.query.filter_by(id=id).first()

    type_model.slug = request.form.get('slug')
    type_model.label = request.form.get('label')
    db_session.add(type_model)
    db_session.commit()

    if type_model.id:
        flash('Данные сохранены')
        return redirect(url_for('type.index'))
    else:
        return redirect(url_for('type.create'))
