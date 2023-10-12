from .app import app, db
import tuto.views
import tuto.commands
import tuto.models
# import os.path

# def mkpath (p):
#     return os.path.normpath(
#         os.path.join(
#             os.path.dirname(__file__),p))

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     'sqlite :/// '+mkpath('../ myapp.db'))
# db = SQLAlchemy(app)