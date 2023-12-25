#!/usr/bin/python3
'''flask script'''

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text=None):
        """Displays the return message"""
        string = text.replace('_', ' ')
        return 'C {}'.format(string)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000', debug=True)
