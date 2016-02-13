# coding: utf-8

from flask import Blueprint
from flask import render_template
from flask.ext.wtf import Form
from flaskckeditor import CKEditor
from wtforms import SubmitField, TextAreaField
import sys


demo = Blueprint(
    'demo',
    __name__,
    static_folder = '/Users/apple/hack/flask-ckeditor/examples/blueprint/static'
)


reload(sys)
sys.setdefaultencoding('utf-8')


class EditForm(Form, CKEditor):
    body = TextAreaField()
    submit = SubmitField('submit')


@demo.route('/edit')
def edit():
    form = EditForm()
    return render_template('edit.html', form=form)


@demo.route('/ckupload/', methods=['OPTIONS', 'POST'])
def ckupload():
    form = EditForm()
    response = form.upload(endpoint=demo)
    return response
