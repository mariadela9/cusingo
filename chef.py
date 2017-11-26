from flask import Blueprint, render_template, request, session, redirect, url_for
from model import *

chef = Blueprint('chef', __name__)



@chef.route('/new', strict_slashes=False)
def chef_signup():
    return render_template('chefsignup.html')


@chef.route('/', methods=['POST'], strict_slashes=False)
def chef_create():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    hours = request.form['hours']
    pay = 9
    if set_new(email, username, password):
        if set_chef(email, pay, hours):
            session['username'] = username
            return render_template('chef_menu.html', user=session['username'])
    return render_template('chefsignup.html', error=True, username=username)
