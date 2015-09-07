# encoding: utf-8

from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'I hate flask!'


from demo import demo
app.register_blueprint(demo, url_prefix='/demo')


if __name__ == "__main__":
    app.run(debug=True)
