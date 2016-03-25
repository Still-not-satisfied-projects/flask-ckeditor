# coding: utf-8
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, StringField
from flaskckeditor import CKEditor


class CKEditorForm(Form, CKEditor):
    title =  StringField()
    ckdemo = TextAreaField()
    submit = SubmitField('submit')

