from flask import Blueprint, render_template, request, session, redirect
from model import *

order = Blueprint('order', __name__)


@order.route('/new', strict_slashes=False)
def new_order():
    pl = get_plates()
    dr = get_drinks()
    return render_template('placeorder.html', user=session['username'], list=pl, list2=dr)


@order.route('/plate/<costumer_id>/<order_id>', methods=['GET','POST'], strict_slashes=False)
def place_order(costumer_id, order_id):
    pl = get_plates()
    dr = get_drinks()
    total = get_total
    if request.method == 'POST':
        category = "any"
        if set_foodOrder(category,total):
            update_kitchen(kitchen_id[1])
            return render_template('show_schedulesuccess.html', user=session['username'])
        return "You have already scheduled this kitchen at that time, please select a different one"
    else:
        return render_template('placeorder.html', user=session['username'], list=pl, list2=dr)


@order.route('/drink/<costumer_id>/<kitchen_id>', methods=['GET','POST'], strict_slashes=False)
def place_order(costumer_id, kitchen_id):
    pl = get_plates()
    dr = get_drinks()
    if request.method == 'POST':
        time = "5:00pm"
        if set_schedule(kitchen_id, chef_id,time):
            update_kitchen(kitchen_id[1])
            return render_template('show_schedulesuccess.html', user=session['username'])
        return "You have already scheduled this kitchen at that time, please select a different one"
    else:
        return render_template('placeorder.html', user=session['username'], list=pl, list2=dr)
