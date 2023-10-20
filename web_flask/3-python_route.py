#!/usr/bin/python3
'''a script that starts a Flask web application:
    Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:'''
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    '''returns hello bnb'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_bnb():
    '''returns hello bnb'''
    return "HBNB"


@app.route('/c/<text>')
def display_c_is_fun(text):
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text='is cool'):
    return f"Python {escape(text).replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
