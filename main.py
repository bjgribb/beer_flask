from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    names = ['Brian', 'Sarah', 'Joelle']
    return render_template('index.html', names=names)

@app.route('/flask_test')
def testing():
    return 'you got to the testing route'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello ' + name + '!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
