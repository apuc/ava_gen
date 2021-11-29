from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.base import Base, db_session
from db.models import Figure, Crud
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
    return render_template('admin/figure/form.html', figure_model=figure_model)


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

    return render_template('admin/figure/form.html', figure_model=figure_model)


@figure_page.route('/figure/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    if id == 'None':
        figure_model = Figure()
    else:
        figure_model = Figure.query.filter_by(id=id).first()

    figure_model.type = request.form.get('type')
    figure_model.age = request.form.get('age')
    figure_model.sex = request.form.get('sex')
    figure_model.rnd_fill = request.form.get('rnd_fill')
    db_session.add(figure_model)
    db_session.commit()

    if figure_model.id:
        flash('Данные сохранены')
        return redirect(url_for('figure.index'))
    else:
        return redirect(url_for('figure.create'))
