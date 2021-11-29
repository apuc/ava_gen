from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.base import Base, db_session
from db.models import Fill, Crud
from sqlalchemy import select, func, Integer, Table, Column, MetaData

fill_page = Blueprint('fill', __name__, template_folder='templates')


@fill_page.route('/fill', defaults={'current_page': 1})
@fill_page.route('/fill/<current_page>')
def index(current_page):
    fills = Fill.query.all()
    crud = Crud(Fill)
    print(crud.get_total())
    return render_template('admin/fill/index.html', fills=fills)


@fill_page.route('/fill/create', methods=['GET'])
def create():
    fill_model = Fill()
    return render_template('admin/fill/form.html', fill_model=fill_model)


@fill_page.route('/fill/remove/<id>')
def remove(id):
    fill_model = Fill.query.filter_by(id=id).first()
    db_session.delete(fill_model)
    db_session.commit()

    flash('Запись удалена')
    return redirect(url_for('fill.index'))


@fill_page.route('/fill/edit/<id>')
def edit(id):
    fill_model = Fill.query.filter_by(id=id).first()

    return render_template('admin/fill/form.html', fill_model=fill_model)


@fill_page.route('/fill/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    if id == 'None':
        fill_model = Fill()
    else:
        fill_model = Fill.query.filter_by(id=id).first()

    fill_model.value = request.form.get('value')
    db_session.add(fill_model)
    db_session.commit()

    if fill_model.id:
        flash('Данные сохранены')
        return redirect(url_for('fill.index'))
    else:
        return redirect(url_for('fill.create'))
