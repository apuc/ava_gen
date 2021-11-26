from flask import Flask, render_template
from admin.figure.routes import figure_page
from db.base import db_session

app = Flask(__name__)
app.register_blueprint(figure_page, url_prefix='/admin')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.debug = True
    app.run()
