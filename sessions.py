from flask import Blueprint, render_template, request, session, redirect, url_for
from model import *

sessions = Blueprint('sessions', __name__)


@sessions.route('/new', strict_slashes=False)
def login_form():
    return render_template('login.html')


@sessions.route('/', methods=['POST'] , strict_slashes=False)
def login():
    username = request.form['username']
    password = request.form['password']
    if check_user(username, password):
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('login.html', username=username, error=True)


@sessions.route('/delete', strict_slashes=False)
def logout():
    session.pop('username', None)
    return render_template('logout.html')