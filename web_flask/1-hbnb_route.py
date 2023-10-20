#!/usr/bin/python3
'''a script that starts a Flask web application:
    Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    '''returns hello bnb'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_bnb():
    '''returns hello bnb'''
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
