from flask import Blueprint, render_template, request, session, redirect, url_for
from model import *

sessions = Blueprint('sessions', __name__)


@sessions.route('/new', strict_slashes=False)
def login_form():
    return render_template('login.html')


@sessions.route('/', methods=['POST'] , strict_slashes=False)
def login():
    email = request.form['username']
    password = request.form['password']
    if check_user(email, password):
        session['username'] = email
        if check_customer(email):
            render_template('customer_menu.html', username=email)
        elif check_chef(email):
            render_template('chef_menu.html', username=email)
        elif check_driver(email):
            render_template('driver_menu.html', username=email)
        return redirect(url_for('index'))
    return render_template('login.html', username=email, error=True)


@sessions.route('/delete', strict_slashes=False)
def logout():
    session.pop('username', None)
    return render_template('logout.html')