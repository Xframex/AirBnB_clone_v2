#!/usr/bin/python3
"""Module"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Display message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays message"""
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
