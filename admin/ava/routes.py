import os
from config import ROOT_DIR
from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.models import Ava, Crud
from generator.generate import generate
from services.AvaService import AvaService

ava_page = Blueprint('ava', __name__, template_folder='templates')


@ava_page.route('/ava', defaults={'current_page': 1})
@ava_page.route('/ava/<current_page>')
def index(current_page):
    crud = Crud(Ava)
    crud.pagination(int(request.args.get('page', 1)), 50)
    return render_template('admin/ava/index.html', crud=crud)


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


@ava_page.route('/ava/gen', methods=['POST']    )
def gen():
    url = generate(ROOT_DIR)
    host = os.getenv("HOST")
    url = f"{host}{url}"
    dct = dict(
        url = url,
    )
    return dct