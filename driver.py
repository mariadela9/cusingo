from flask import Blueprint, render_template, request, session, redirect, url_for
from model import *

driver = Blueprint('driver', __name__)



@driver.route('/new', strict_slashes=False)
def driver_signup():
    return render_template('driversignup.html')


@driver.route('/', methods=['POST'], strict_slashes=False)
def driver_create():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    model = request.form['carmodel']
    make = request.form['carmake']
    year = request.form['caryear']
    hours = request.form['hours']
    pay = 9
    if set_new(email, username, password):
        if set_driver(email, pay, hours):
            if set_car(email, model, make, year):
                session['username'] = username
                return render_template('driver_menu.html', user=session['username'])
    return render_template('driversignup.html', error=True, username=username)
