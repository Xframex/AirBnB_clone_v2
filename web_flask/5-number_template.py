#!/usr/bin/python3
"""base templete handling"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """return message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays the return message"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text=None):
    """Displays the return message"""
    string = text.replace('_', ' ')
    return 'C {}'.format(string)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Displays the return message"""
    string = text.replace('_', ' ')
    return 'Python {}'.format(string)


@app.route('/number/<int:n>', strict_slashes=False)
def is_an_int(n):
    """Displays a message when recives  integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def templates_an_int(n):
    """Display  HTML when recives an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
