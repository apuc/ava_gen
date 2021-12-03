from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.models import Fill, Crud
from services.FillService import FillService

fill_page = Blueprint('fill', __name__, template_folder='templates')


@fill_page.route('/fill', defaults={'current_page': 1})
@fill_page.route('/fill/<current_page>')
def index(current_page):
    crud = Crud(Fill)
    crud.pagination(int(request.args.get('page', 1)), 5)
    return render_template('admin/fill/index.html', crud=crud)


@fill_page.route('/fill/create', methods=['GET'])
def create():
    fill_model = Fill()
    return render_template('admin/fill/form.html', fill_model=fill_model)


@fill_page.route('/fill/remove/<id>')
def remove(id):
    FillService.remove(id)
    flash('Запись удалена')
    return redirect(url_for('fill.index'))


@fill_page.route('/fill/edit/<id>')
def edit(id):
    fill_model = FillService.get(id)

    return render_template('admin/fill/form.html', fill_model=fill_model)


@fill_page.route('/fill/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    params = dict(value = request.form.get('value'))
    FillService.save(id, **params)

    flash('Данные сохранены')
    return redirect(url_for('fill.index'))
