from flask import Blueprint, render_template, request, session, redirect
from model import *

order = Blueprint('order', __name__)

@order.route('/new', strict_slashes=False)
def new_order():
    foods = get_foods()
    return render_template('placeorder.html', user=session['username'], list=foods)


@order.route('/<customer_id>/<order_id>', methods=['GET','POST'], strict_slashes=False)
def place_order(customer_id,order_id):
    foods = get_foods()
    if request.method == 'POST':
        price = get_orderprice(order_id)
        if set_finalorder(order_id, price):
            return render_template('show_placeordersuccess.html', user=session['username'])
        return "Unable to place order, might not be available at the time"
    else:
        return render_template('placeorder.html', user=session['username'], list=foods)
