import os.path
from flask import Flask
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOVAL'] = True
bootstrap = Bootstrap5(app)

def mkpath (p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),p))

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite://'+mkpath('myapp.db'))
db = SQLAlchemy (app)

