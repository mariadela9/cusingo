from flask import Blueprint, render_template, request, session, redirect, url_for
from model import *

user = Blueprint('user', __name__)


@user.route('/new', strict_slashes=False)
def user_signup():
    return render_template('signup.html')


@user.route('/', methods=['POST'], strict_slashes=False)
def user_create():
    username = request.form['username']
    password = request.form['password']
    if set_new(username, password):
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('signup.html', error=True, username=username)