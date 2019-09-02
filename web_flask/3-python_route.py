#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    '''path /'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_world2():
    '''path /hbnb'''
    return 'HBNB'


@app.route('/c/<text>')
def show_text_c(text):
    '''path /c/<text>'''
    return 'C %s' % escape(text).replace('_', ' ')


@app.route('/python/<text>')
@app.route('/python')
def show_text_python(text="is_cool"):
    '''path /python/<text>'''
    return 'Python %s' % escape(text).replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
