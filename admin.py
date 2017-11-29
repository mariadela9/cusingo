from flask import Blueprint, render_template, request, session, redirect, url_for
from model import *

admin = Blueprint('admin', __name__)

@admin.route('/new', strict_slashes=False)
def admin_login():
    return render_template('admin_login.html')

@admin.route('/', methods=['POST'] , strict_slashes=False)
def admin_validate():
    email = request.form['username']
    password = request.form['password']
    if email == 'admin' :
        if password == 'password':
            return render_template('admin.html')
