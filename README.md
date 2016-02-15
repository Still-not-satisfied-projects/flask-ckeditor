Flask-CKEditor
===
a [flask](https://github.com/mitsuhiko/flask) module for [CKEditor](http://ckeditor.com) integration

### Flask-CKEditor Demo
#### demo => http://115.28.152.113:520/appDemo/
#### code => https://github.com/neo1218/flask-ckeditor-demo

### Situation 1: Basic Usage
#### Step1: Clone the [CKEditor](https://github.com/neo1218/Configured-CKEditor) I Have Configured.
#### Step2: Writing Forms(In Flask-WTF Case)

    from flask_wtf import Form
    from wtforms import TextAreaField, SubmitField, StringField

    class CKEditorForm(Form):
        title =  StringField()
        ckdemo = TextAreaField()
        submit = SubmitField('submit')

#### Step3: Replace the Form to CKEditor

    <script src="/static/ckeditor/ckeditor.js" type="text/javascript"></script>

    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.title }}
        {{ form.ckdemo(class='ckeditor') }}
        {{ form.submit }}
    </form>

### Situation 2: Open (file/img)Upload Interface
#### Step1: Upload Class Inheritance

    from flask_wtf import Form
    from wtforms import TextAreaField, SubmitField, StringField
    from flaskckeditor import CKEditor

    class CKEditorForm(Form, CKEditor):
        title =  StringField()
        ckdemo = TextAreaField()
        submit = SubmitField('submit')

#### Step2: Write Upload View Function

    from "forms_module" import CKEditorForm

    @app.route("/ckupload/")
    def ckupload():
        form = CKEditor()
        res = form.upload(endpoint=app)
        return res

### Situation 3: Use Blueprint

1. 配置蓝图的static_folder
2. 修改上传路由

### API
#### :class: CKEditor
#### :func: gen_rnd_file()
#### :func: upload()

### LICENSE
MIT: check [LICENSE](https://github.com/neo1218/flask-ckeditor/blob/master/LICENSE) for more detail

### Thanks
