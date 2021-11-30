from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.base import Base, db_session
from db.models import Crud, Figure, Fill, Path
from sqlalchemy import select, func, Integer, Table, Column, MetaData

path_page = Blueprint('path', __name__, template_folder='templates')


@path_page.route('/path', defaults={'current_page': 1})
@path_page.route('/path/<current_page>')
def index(current_page):
    paths = Path.query.all()
    crud = Crud(Path)
    print(crud.get_total())
    return render_template('admin/path/index.html', paths=paths)


@path_page.route('/path/create', methods=['GET'])
def create():
    path_model = Path()
    fills = Fill().query.all()
    figures = Figure().query.all()
    return render_template('admin/path/form.html', path_model=path_model, fills = fills, figures = figures)


@path_page.route('/path/remove/<id>')
def remove(id):
    path_model = Path.query.filter_by(id=id).first()
    db_session.delete(path_model)
    db_session.commit()

    flash('Запись удалена')
    return redirect(url_for('path.index'))


@path_page.route('/path/edit/<id>')
def edit(id):
    path_model = Path.query.filter_by(id=id).first()
    select_fill = Fill().query.filter_by(id=path_model.fill_id).first()
    fills = Fill().query.filter(Fill.id != path_model.fill_id).all()
    select_figure = Figure().query.filter_by(id=path_model.figure_id).first()
    figures = Figure().query.filter(Figure.id != path_model.figure_id).all()
    return render_template('admin/path/form.html', path_model=path_model, select_fill=select_fill, fills = fills, select_figure=select_figure, figures=figures)


@path_page.route('/path/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    if id == 'None':
        path_model = Path()
    else:
        path_model = Path.query.filter_by(id=id).first()

    path_model.d = request.form.get('d')
    path_model.extend_fill = request.form.get('extend_fill')
    path_model.fill_id = request.form.get('fill_id')
    path_model.priority = request.form.get('priority')
    path_model.figure_id = request.form.get('figure_id')
    path_model.status = request.form.get('status')
    db_session.add(path_model)
    db_session.commit()

    if path_model.id:
        flash('Данные сохранены')
        return redirect(url_for('path.index'))
    else:
        return redirect(url_for('path.create'))
