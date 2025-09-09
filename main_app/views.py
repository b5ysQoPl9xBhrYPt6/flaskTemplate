import flask
from project.loadenv import *

def render_main():
    return flask.render_template('home.html', name = get_env('KEY1'))

