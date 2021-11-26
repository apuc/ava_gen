from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.base import Base, db_session
from db.models import Type
from sqlalchemy import select, insert

type_page = Blueprint('type', __name__, template_folder='templates')


@type_page.route('/type')
def index():
    type_model = Type()
    types = type_model.query.all()
    return render_template('admin/type/index.html', types=types)


@type_page.route('/type/create', methods=['GET', 'POST'])
def create():
    type_model = Type()
    if request.method == 'POST':
        type_model.slug = request.form.get('slug')
        type_model.label = request.form.get('label')
        db_session.add(type_model)
        db_session.commit()
        if type_model.id:
            flash('Запись добавлена')
            return redirect(url_for('type.index'))
        else:
            return redirect(url_for('type.create'))

        # if insert_type:
        #     return redirect('type.index')

    else:
        return render_template('admin/type/form.html')
