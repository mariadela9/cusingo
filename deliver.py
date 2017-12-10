from flask import Blueprint, render_template, request, session, redirect
from model import *

deliver = Blueprint('deliver', __name__)


@deliver.route('/new', strict_slashes=False)
def new_delivery():
    od = get_orders()
    return render_template('deliverorder.html', user=session['username'], list=od)


@deliver.route('/<driver_id>/<order_id>', methods=['GET','POST'], strict_slashes=False)
def set_delivery(driver_id, order_id):
    od = get_orders()
    if request.method == 'POST':
        if set_deliver(driver_id, order_id):
            return render_template('show_deliverysuccess.html', user=session['username'])
        return "Order has been picked up by a different driver."
    else:
        return render_template('deliverorder.html', user=session['username'], list=od)
