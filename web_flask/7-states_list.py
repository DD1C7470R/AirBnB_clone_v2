#!/usr/bin/python3
'''a script that starts a Flask web application:
    Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:'''
from flask import Flask, render_template
from markupsafe import escape
from models import storage

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


@app.route('/number/<int:n>')
def display_n(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def display_n_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    num = {}
    num['value'] = n
    if n % 2 == 0:
        num['type'] = 'even'
    else:
        num['type'] = 'odd'
    return render_template('6-number_odd_or_even.html', num=num)


@app.route('/states_list')
def state_list():
    from models.state import State

    proc_states = []
    states = storage.all(State)
    for key, val in states.items():
        proc_states.append(val)
    return render_template(
            '7-states_list.html',
            states=sorted(proc_states, key=lambda x: x.name)
            )


@app.teardown_appcontext
def tear_down(error):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
