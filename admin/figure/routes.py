from flask import Blueprint, render_template
from db.base import Base
from db.models import Figure

figure_page = Blueprint('figure', __name__, template_folder='templates')


@figure_page.route('/figure')
def index():
    figures_model = Figure()
    figures = figures_model.query.all()
    return render_template('admin/figure/index.html', figures=figures)


@figure_page.route('/figure/create')
def create():
    figures_model = Figure()
    figures = figures_model.query.all()
    return render_template('admin/figure/form.html', figures=figures)
