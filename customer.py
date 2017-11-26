from flask import Blueprint, render_template, request, session, redirect, url_for
from model import *

customer = Blueprint('customer', __name__)



@customer.route('/new', strict_slashes=False)
def customer_signup():
    return render_template('customersignup.html')


@customer.route('/', methods=['POST'], strict_slashes=False)
def customer_create():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    address = request.form['address']
    if set_new(email, username, password):
        if set_customer(email, address):
            session['username'] = username
            return render_template('customer_menu.html', user=session['username'])
    return render_template('customersignup.html', error=True, username=username)

