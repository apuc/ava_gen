from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.base import Base, db_session
from db.models import Figure, Crud, Type
from services.FigureService import FigureService
from services.TypeService import TypeService


figure_page = Blueprint('figure', __name__, template_folder='templates')


@figure_page.route('/figure', defaults={'current_page': 1})
@figure_page.route('/figure/<current_page>')
def index(current_page):
    figures = FigureService.find()
    for i in range(len(figures)):
        figures[i].type_label = TypeService.get(figures[i].type_id).label
    # crud = Crud(Figure)
    # print(crud.get_total())
    return render_template('admin/figure/index.html', figures=figures)


@figure_page.route('/figure/create', methods=['GET'])
def create():
    figure_model = Figure()
    types = TypeService.find()
    return render_template('admin/figure/form.html', figure_model=figure_model, types=types)


@figure_page.route('/figure/remove/<id>')
def remove(id):
    FigureService.remove(id)

    flash('Запись удалена')
    return redirect(url_for('figure.index'))


@figure_page.route('/figure/edit/<id>')
def edit(id):
    figure_model = FigureService.get(id)
    select_type = TypeService.get(figure_model.type_id)
    types = Type().query.filter(Type.id != figure_model.type_id).all()
    return render_template('admin/figure/form.html', figure_model=figure_model, types=types, select_type=select_type)


@figure_page.route('/figure/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    params = dict(
            type_id=request.form.get('type_id'),
            age=request.form.get('age'),
            rnd_fill=request.form.get('rnd_fill'),
            sex=request.form.get('sex')
        )
    error = FigureService.save(id, **params)
    if(error):
        flash(error['message'])
        if error['is_edit']:
            return redirect(url_for('figure.edit', id = id))
        else:
            return redirect(url_for('figure.create'))
    else:
        flash('Данные сохранены')
        return redirect(url_for('figure.index'))
