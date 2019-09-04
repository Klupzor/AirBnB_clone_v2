#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask, escape, render_template
from models import storage
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


@app.route('/number/<int:n>')
def show_number(n):
    '''Print number'''
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def show_template_number(n):
    '''Show number on template'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def show_template_number_eo(n):
    '''Show number on template and even|odd'''
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, txt="even")
    return render_template('6-number_odd_or_even.html', n=n, txt="odd")


@app.route('/states_list')
def states_list():
    '''List of all States'''
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def city_list():
    '''List of all cities of States'''
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>')
@app.route('/states')
def states(id=None):
    '''List of all of States id'''
    if (id):
        states = storage.all('State')
        try:
            cities = states["State." + id]
        except KeyError:
            return render_template('9-states.html', error="Not found!", id=id)
        return render_template('9-states.html', states=cities, id=id)
    else:
        states = storage.all('State').values()
        return render_template('9-states.html', states=states)


@app.teardown_appcontext
def close_session(cls):
    '''Close session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
