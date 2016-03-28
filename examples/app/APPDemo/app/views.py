# coding: utf-8
from . import app
from flask import render_template, redirect, url_for
from .forms import CKEditorForm


@app.route('/appdemo/', methods=['GET'])
def appDemo():
    """demo view"""
    form = CKEditorForm()
    # if form.validate_on_submit():
    #     return redirect(url_for('appDemo'))
    return render_template('demo.html', form=form)


@app.route('/ckupload/', methods=['POST'])
def ckupload():
    """file/img upload interface"""
    form = CKEditorForm()
    response = form.upload(name=app)
    return response

