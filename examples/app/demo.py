# coding: utf-8

from flask import Flask, render_template
from flask.ext.wtf import Form
from flaskckeditor import CKEditor
from wtforms import SubmitField, TextAreaField
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'I hate flask, it is hard to guess'


class EditForm(Form, CKEditor):
    body = TextAreaField()
    submit = SubmitField('submit')


@app.route('/edit')
def edit():
    form = EditForm()
    return render_template('edit.html', form=form)


@app.route('/ckupload/', methods=['OPTIONS', 'POST'])
def ckupload():
    form = EditForm()
    response = form.upload(endpoint=app)
    return response


if __name__ == '__main__':
    app.run(debug=True)
