#!/usr/bin/python3
'''a script that starts a Flask web application:'''

from web_flask import app


@app.route('/')
def hello_bnb():
    '''returns hello bnb'''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
