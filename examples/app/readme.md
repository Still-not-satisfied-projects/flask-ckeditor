# App Demo

> Flask-CKEditor Demo in App

## Build
### 1. Create Flask Project
[mana](https://github.com/neo1218/mana.git)

    $ mana init APPDemo

### 2. Download CKEditor
[CKEditor](http://ckeditor.com/) <br/>
Download CKEditor in static folder (/static/ckeditor)

### 3. Config CKEditor
[config.js](http://www.oschina.net/code/snippet_559362_10887)

### 4. Write CKEditor Form
app/forms.py

    from flask_wtf import Form
    from wtforms import TextAreaField, SubmitField, StringField
    from flaskckeditor import CKEditor

    class CKEditorForm(Form, CKEditor):
        title =  StringField()
        ckdemo = TextAreaField()
        submit = SubmitField('submit')

### 5. Replace the Form 2 CKEditor and set upload url
example for flask-wtf-form

    <head>
        <script src="/static/ckeditor/ckeditor.js" type="text/javascript"></script>
    </head>

    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.title(class='form-control', placeholder='appDemo', type='text') }}
        {{ form.ckdemo(class='ckeditor') }}
        <script type="text/javascript">
            CKEDITOR.replace("ckdemo", {
                filebrowserUploadUrl: '/ckupload/',
                filebrowserImageUploadUrl: '/ckupload/'
            });
        </script>
        {{ form.submit(class="btn btn-default") }}
    </form>

### 6. Open file/img upload interface
app/views.py

    from .forms import CKEditorForm

    @app.route('/ckupload/', methods=['POST', 'OPTIONS'])
    def ckupload():
        """file/img upload interface"""
        form = CKEditorForm()
        response = form.upload(endpoint=app)
        return response

## Demo



