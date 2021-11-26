from flask import Flask, render_template
from admin.figure.routes import figure_page
from admin.type.routes import type_page
from db.base import db_session

app = Flask(__name__)
app.secret_key = b'6VJ3NyYGP8rnPpWp'
app.register_blueprint(figure_page, url_prefix='/admin')
app.register_blueprint(type_page, url_prefix='/admin')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.debug = True
    app.run()
