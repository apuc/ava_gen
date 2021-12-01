from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.base import Base, db_session
from db.models import Ava, Crud
from sqlalchemy import select, func, Integer, Table, Column, MetaData
import uuid

ava_page = Blueprint('ava', __name__, template_folder='templates')


@ava_page.route('/ava', defaults={'current_page': 1})
@ava_page.route('/ava/<current_page>')
def index(current_page):
    avatars = Ava.query.all()
    crud = Crud(Ava)
    print(crud.get_total())
    return render_template('admin/ava/index.html', avatars=avatars)


@ava_page.route('/ava/create', methods=['GET'])
def create():
    ava_model = Ava()
    return render_template('admin/ava/form.html', ava_model=ava_model)


@ava_page.route('/ava/remove/<id>')
def remove(id):
    ava_model = Ava.query.filter_by(id=id).first()
    db_session.delete(ava_model)
    db_session.commit()

    flash('Запись удалена')
    return redirect(url_for('ava.index'))


@ava_page.route('/ava/edit/<id>')
def edit(id):
    ava_model = Ava.query.filter_by(id=id).first()

    return render_template('admin/ava/form.html', ava_model=ava_model)


@ava_page.route('/ava/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    if id == 'None':
        ava_model = Ava()
        ava_model.id = str(uuid.uuid1())
        is_edit = False
    else:
        ava_model = Ava.query.filter_by(id=id).first()
        is_edit = True

    if(int(request.form.get('age')) < 1):
        flash('Возраст не может быть меньше 1')
        if is_edit:
            return redirect(url_for('ava.edit', id = ava_model.id))
        else:
            return redirect(url_for('ava.create'))

    ava_model.age = request.form.get('age')

    if(int(request.form.get('sex')) == 0 or int(request.form.get('sex')) == 1):
        ava_model.sex = request.form.get('sex')
    else:
        flash('Пол не определен')
        if is_edit:
            return redirect(url_for('ava.edit', id = ava_model.id))
        else:
            return redirect(url_for('ava.create'))

    db_session.add(ava_model)
    db_session.commit()

    if ava_model.id:
        flash('Данные сохранены')
        return redirect(url_for('ava.index'))
    else:
        return redirect(url_for('ava.create'))
