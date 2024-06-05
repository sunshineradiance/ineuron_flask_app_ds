# app.py
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello1')
def hello_world1():
    return 'Hello, World!1'

@app.route('/hello2')
def hello_world2():
    return 'Hello, World!2'

@app.route('/test_func')
def test1():
    a = 5 + 6
    return "this is my first test func in flask {}".format(a)

@app.route("/input_url1")
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
