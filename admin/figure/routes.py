from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.base import Base, db_session
from db.models import Figure, Crud, Type
from sqlalchemy import select, func, Integer, Table, Column, MetaData

figure_page = Blueprint('figure', __name__, template_folder='templates')


@figure_page.route('/figure', defaults={'current_page': 1})
@figure_page.route('/figure/<current_page>')
def index(current_page):
    figures = Figure.query.all()
    crud = Crud(Figure)
    print(crud.get_total())
    return render_template('admin/figure/index.html', figures=figures)


@figure_page.route('/figure/create', methods=['GET'])
def create():
    figure_model = Figure()
    types = Type().query.all()
    return render_template('admin/figure/form.html', figure_model=figure_model, types=types)


@figure_page.route('/figure/remove/<id>')
def remove(id):
    figure_model = Figure.query.filter_by(id=id).first()
    db_session.delete(figure_model)
    db_session.commit()

    flash('Запись удалена')
    return redirect(url_for('figure.index'))


@figure_page.route('/figure/edit/<id>')
def edit(id):
    figure_model = Figure.query.filter_by(id=id).first()
    select_type = Type().query.filter_by(id=figure_model.type_id).first()
    types = Type().query.filter(Type.id != figure_model.type_id).all()
    return render_template('admin/figure/form.html', figure_model=figure_model, types=types, select_type=select_type)


@figure_page.route('/figure/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    if id == 'None':
        figure_model = Figure()
        is_edit = False
    else:
        figure_model = Figure.query.filter_by(id=id).first()
        is_edit = True

    figure_model.type_id = request.form.get('type_id')

    if(int(request.form.get('age')) < 1):
        flash('Возраст не может быть меньше 1')
        if is_edit:
            return redirect(url_for('figure.edit', id = figure_model.id))
        else:
            return redirect(url_for('figure.create'))

    figure_model.age = request.form.get('age')

    if(int(request.form.get('sex')) == 0 or int(request.form.get('sex')) == 1):
        figure_model.sex = request.form.get('sex')
    else:
        flash('Пол не определен')
        if is_edit:
            return redirect(url_for('figure.edit', id = figure_model.id))
        else:
            return redirect(url_for('figure.create'))

    figure_model.rnd_fill = request.form.get('rnd_fill')
    db_session.add(figure_model)
    db_session.commit()

    if figure_model.id:
        flash('Данные сохранены')
        return redirect(url_for('figure.index'))
    else:
        return redirect(url_for('figure.create'))
