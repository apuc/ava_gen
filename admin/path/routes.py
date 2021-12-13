from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.base import Base, db_session
from db.models import Crud, Figure, Fill, Path
from services.FigureService import FigureService
from services.FillService import FillService

from services.PathService import PathService
from services.TypeService import TypeService

path_page = Blueprint('path', __name__, template_folder='templates')


@path_page.route('/path', defaults={'current_page': 1})
@path_page.route('/path/<current_page>')
def index(current_page):
    crud = Crud(Path)
    crud.pagination(int(request.args.get('page', 1)), 50)
    for i in range(len(crud.items)):
        crud.items[i].fill = FillService.get(crud.items[i].fill_id).value
        figure = FigureService.get(crud.items[i].figure_id)
        crud.items[i].figure_label = figure.label
        crud.items[i].figure_sex = figure.sex
        crud.items[i].figure_age = figure.age
    return render_template('admin/path/index.html', crud=crud)


@path_page.route('/path/create', methods=['GET'])
def create():
    path_model = Path()
    fills = FillService().find()
    figures = FigureService().find()
    for i in range(len(figures)):
        figures[i].type_label = TypeService.get(figures[i].type_id).label
    return render_template('admin/path/form.html', path_model=path_model, fills = fills, figures = figures)


@path_page.route('/path/remove/<id>')
def remove(id):
    PathService.remove(id)

    flash('Запись удалена')
    return redirect(url_for('path.index'))


@path_page.route('/path/edit/<id>')
def edit(id):
    path_model = PathService.get(id)
    select_fill = FillService().get(path_model.fill_id)
    fills = Fill().query.filter(Fill.id != path_model.fill_id).all()
    select_figure = FigureService().get(path_model.figure_id)
    select_figure.type_label = TypeService.get(select_figure.type_id).label
    figures = Figure().query.filter(Figure.id != path_model.figure_id).all()
    for i in range(len(figures)):
        figures[i].type_label = TypeService.get(figures[i].type_id).label
    return render_template('admin/path/form.html', path_model=path_model, select_fill=select_fill, fills = fills, select_figure=select_figure, figures=figures)


@path_page.route('/path/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    
    params = dict(
        d = request.form.get('d'),
        extend_fill = request.form.get('extend_fill'),
        fill_id = request.form.get('fill_id'),
        priority = request.form.get('priority'),
        figure_id = request.form.get('figure_id'),
        status = request.form.get('status')
    )

    error = PathService.save(id, **params)
    if(error):
        flash(error['message'])
        if error['is_edit']:
            return redirect(url_for('path.edit', id = id))
        else:
            return redirect(url_for('path.create'))
    else:
        flash('Данные сохранены')
        return redirect(url_for('path.index'))
