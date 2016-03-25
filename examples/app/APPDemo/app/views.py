# coding: utf-8
from . import app
from flask import render_template, redirect, url_for
from .forms import CKEditorForm


@app.route('/appDemo/', methods=['POST', 'GET'])
def appDemo():
    """demo view"""
    form = CKEditorForm()
    if form.validate_on_submit():
        return redirect(url_for('appDemo'))
    return render_template('demo.html', form=form)


@app.route('/ckupload/', methods=['POST', 'OPTIONS'])
def ckupload():
    """file/img upload interface"""
    form = CKEditorForm()
    response = form.upload(endpoint=app)
    return response

