#!/usr/bin/env python
# encoding: utf-8

"""
    flask-ckeditor
    ~~~~~~~~~~~~~~

        在flask中集成ckeditor编辑器
"""

# from flask import what I  want
from flask import request, url_for, make_response
import os
import random
import datetime


class CKEditor(object):
    """
    class CKEditor
    ~~~~~~~~~~~~~~

        from flask import Flask
        from flask.ext.ckeditor import CKEditor
        from flask.ext.wtf import Form
        from wtforms import SubmitField, TextareaField

        app = Flask(__name__)

        class EditForm(Form, CKEditor):
            body = TextareaField()
            submit = SubmitField('submit')

        @app.route('/ckupload/', methods=['OPTIONS', 'POST'])
        def ckupload():
            # 实现上传接口
            form = EditForm()
            form.upload(endpoint=app)
    """
    def __init__(self):
        pass

    def gen_rnd_filename(self):
        """依据上传日期生成随机文件名"""
        filename_prefix = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return "%s%s" % (filename_prefix, str(random.randrange(1000,10000)))

    def upload(self, endpoint=None):
        """CKEditor 文件(图片、文档) 上传"""
        error = ''
        url = ''
        callback = request.args.get("CKEditorFuncNum")

        if request.method == 'POST' and 'upload' in request.files:
            # /static/upload
            fileobj = request.files['upload']
            fname, fext = os.path.splitext(fileobj.filename)
            rnd_name = '%s%s' % (self.gen_rnd_filename(), fext)

            filepath = os.path.join(endpoint.static_folder, 'upload', rnd_name)

            # 检查路径是否存在，不存在则创建
            dirname = os.path.dirname(filepath)
            if not os.path.exists(dirname):
                try:
                    os.makedirs(dirname)
                except:
                    error = 'ERROR_CREATE_DIR'
            elif not os.access(dirname, os.W_OK):
                    error = 'ERROR_DIR_NOT_WRITEABLE'
            if not error:
                fileobj.save(filepath)
                url = url_for('.static', filename='%s/%s' % ('upload', rnd_name))
        else:
            error = 'post error'

        res = """
                <script type="text/javascript">
                window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
                </script>
             """ % (callback, url, error)

        response = make_response(res)
        response.headers["Content-Type"] = "text/html"
        return response
