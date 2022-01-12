from flask import Flask, render_template, send_file, redirect
from admin.figure.routes import figure_page
from admin.type.routes import type_page
from admin.fill.routes import fill_page
from admin.ava.routes import ava_page
from admin.type_fill.routes import type_fill_page
from admin.path.routes import path_page
from db.base import db_session

app = Flask(__name__)
app.secret_key = b'6VJ3NyYGP8rnPpWp'
app.register_blueprint(figure_page, url_prefix='/admin')
app.register_blueprint(type_page, url_prefix='/admin')
app.register_blueprint(fill_page, url_prefix='/admin')
app.register_blueprint(ava_page, url_prefix='/admin')
app.register_blueprint(type_fill_page, url_prefix='/admin')
app.register_blueprint(path_page, url_prefix='/admin')


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/files/<first>/<second>/<full>')
def index(first, second, full):
    try:
        return send_file(f'files/{first}/{second}/{full}')
    except:
        return redirect('/admin/ava')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.debug = True
    app.run()
