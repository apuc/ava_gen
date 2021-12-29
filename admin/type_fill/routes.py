from flask import Blueprint, render_template, request, redirect, url_for, flash
from db.models import Crud, Fill, Type, Type_Fill
from services.FillService import FillService
from services.TypeService import TypeService
from services.Type_FillService import Type_FillService

type_fill_page = Blueprint('TypeFill', __name__, template_folder='templates')


@type_fill_page.route('/TypeFill', defaults={'current_page': 1})
@type_fill_page.route('/TypeFill/<current_page>')
def index(current_page):
    crud = Crud(Type_Fill)
    crud.pagination(int(request.args.get('page', 1)), 50)
    for i in range(len(crud.items)):
        crud.items[i].type = TypeService.get(crud.items[i].type_id).label
        crud.items[i].fill = FillService.get(crud.items[i].fill_id).value
    return render_template('admin/TypeFill/index.html', crud=crud)


@type_fill_page.route('/TypeFill/create', methods=['GET'])
def create():
    type_fill_model = Type_Fill()
    types = TypeService.find()
    fills = FillService.find()
    return render_template('admin/TypeFill/form.html', TypeFill=type_fill_model, types=types, fills=fills)


@type_fill_page.route('/TypeFill/remove/<id>')
def remove(id):
    Type_FillService.remove(id)

    flash('Запись удалена')
    return redirect(url_for('TypeFill.index'))


@type_fill_page.route('/TypeFill/edit/<id>')
def edit(id):
    type_fill_model = Type_FillService.get(id)
    select_type = TypeService.get(type_fill_model.type_id)
    types = Type().query.filter(Type.id != type_fill_model.type_id).all()
    select_fill = FillService.get(type_fill_model.fill_id)
    fills = Fill().query.filter(Type.id != type_fill_model.fill_id).all()
    type_fill_model.fill = FillService.get(type_fill_model.fill_id).value
    return render_template('admin/TypeFill/form.html', TypeFill=type_fill_model, types=types, select_type=select_type, fills=fills, select_fill=select_fill)


@type_fill_page.route('/TypeFill/save', methods=['POST'])
def save():
    id = request.form.get('__id')
    params = dict(
            type_id=request.form.get('type_id'),
            fill_id=request.form.get('fill_id'),
        )
    Type_FillService.save(id, **params)
    flash('Данные сохранены')
    return redirect(url_for('TypeFill.index'))
