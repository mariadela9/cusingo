from flask import Blueprint, render_template, request, session, redirect
from model import *

offer = Blueprint('offer', __name__)


@offer.route('/new', strict_slashes=False)
def new_offer():
    return render_template('offerorder.html', user=session['username'])


@offer.route('/<chef_id>', methods=['GET','POST'], strict_slashes=False)
def place_food(chef_id):
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        orderID = set_foodOrder(price,name,category)
        oID = orderID[0][0]
        if orderID:
            set_make(chef_id, oID)
            return render_template('show_offersuccess.html', user=session['username'])
        return "Unable to place order, might not be available at the time"
    else:
        return render_template('offerorder.html', user=session['username'])
