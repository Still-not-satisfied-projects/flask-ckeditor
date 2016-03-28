# coding: utf-8

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = 'I hate flask, because it is awesome'
toolbar = DebugToolbarExtension(app)


from . import views, forms
