flask-ckeditor
===
### flask后台快速集成ckeditor编辑器

## flask
一个轻量、可扩展、强大的python web 框架<br/>
官方文档: http://flask.pocoo.org/docs/   <br/>
代码仓库: https://github.com/mitsuhiko/flask.git  <br/>

## ckeditor
The best web text editor for everyone<br/>
官方网站: http://ckeditor.com/  <br/>
代码仓库: https://github.com/ckeditor/ckeditor-dev.git  <br/>

## flask-ckeditor
双剑合并，😄

## 使用

### 准备

    1. clone 这个仓库到本地
    2. 将 ckeditor 目录放置在 flask 项目的 static 目录下
    3. 在 static 目录下建立 upload 目录

### 安装

    pip install flaskckeditor

### 集成
#### 1. 在希望集成的html头部引入js文件

    <script src="{{url_for('static', filename='ckeditor/ckeditor.js')}}"></script>

#### 2. 将被替换的表单的class属性设为ckeditor,添加替换脚本

    <form method="post">
        {{ form.hidden_tag() }}
        {{ form.ckeditor_demo(class='ckeditor') }}
        <!-- 替换脚本 -->
        <script type="text/javascript">
            CKEDITOR.replace(
                "ckeditor_demo", {
                    filebrowserUploadUrl: '/ckupload/'
                }
            );
        </script>
        <!---->
        {{ form.submit }}
    <form>

#### 3. 开启上传（图片、文件）接口
3.1: 在表单类中集成 CKEditor 类

    from flaskckeditor import CKEditor
    from flask.ext.wtf import Form
    from wtforms import TextAreaField, SubmitField
    ......
    class EditForm(Form, CKEditor):
        ckeditor_demo = TextAreaField()
        submit = SubmitField('提交')

3.2: 上传路由

    @app.route('/ckupload/')
    def ckupload():
        form = EditForm()
        response = form.upload(endpoint=app)
        return response

现在访问对应html的路由，你会看到漂亮的CKEditor编辑器，并且可以使用它上传文件和图片：）

## API

### CKEditor 类：
#### gen_rnd_filename() 函数
依据时间生成上传文件的随机文件名<br/>

#### upload(endpoint='') 函数
实现 ckeditor 上传功能<br/>
endpoint: 视图函数的端点名，针对蓝图的使用<br/>
