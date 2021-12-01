from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.models import Type, Crud
from services.TypeService import TypeService

type_page = Blueprint('type', __name__, template_folder='templates')


@type_page.route('/type', defaults={'current_page': 1})
@type_page.route('/type/<current_page>')
def index(current_page):
    types = TypeService.find()
    # crud = Crud(Type)
    # print(crud.get_total())
    return render_template('admin/type/index.html', types=types)


@type_page.route('/type/create', methods=['GET'])
def create():
    type_model = Type()
    return render_template('admin/type/form.html', type_model=type_model)


@type_page.route('/type/remove/<id>')
def remove(id):
    TypeService.remove(id)
    flash('Запись удалена')
    return redirect(url_for('type.index'))


@type_page.route('/type/edit/<id>')
def edit(id):
    type_model = TypeService.get(id)
    return render_template('admin/type/form.html', type_model=type_model)


@type_page.route('/type/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    params = dict(
            slug=request.form.get('slug'),
            label=request.form.get('label')
        )
    error = TypeService.save(id, **params)
    if(error):
        flash(error['message'])
        if error['is_edit']:
            return redirect(url_for('type.edit', id = id))
        else:
            return redirect(url_for('type.create'))
    else:
        flash('Данные сохранены')
        return redirect(url_for('type.index'))
