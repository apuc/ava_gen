from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.models import Ava, Crud

from services.AvaService import AvaService

ava_page = Blueprint('ava', __name__, template_folder='templates')


@ava_page.route('/ava', defaults={'current_page': 1})
@ava_page.route('/ava/<current_page>')
def index(current_page):
    avatars = AvaService.find()
    # crud = Crud(Ava)
    # print(crud.get_total())
    return render_template('admin/ava/index.html', avatars=avatars)


@ava_page.route('/ava/create', methods=['GET'])
def create():
    ava_model = Ava()
    return render_template('admin/ava/form.html', ava_model=ava_model)


@ava_page.route('/ava/remove/<id>')
def remove(id):
    AvaService.remove(id)
    flash('Запись удалена')
    return redirect(url_for('ava.index'))


@ava_page.route('/ava/edit/<id>')
def edit(id):
    ava_model = AvaService.get(id)
    return render_template('admin/ava/form.html', ava_model=ava_model)


@ava_page.route('/ava/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    params = dict(
            age=request.form.get('age'),
            sex=request.form.get('sex')
        )
    error = AvaService.save(id, **params)
    if(error):
        flash(error['message'])
        if error['is_edit']:
            return redirect(url_for('ava.edit', id = id))
        else:
            return redirect(url_for('ava.create'))
    else:
        flash('Данные сохранены')
        return redirect(url_for('ava.index'))
