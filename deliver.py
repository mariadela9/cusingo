from flask import Blueprint, render_template, request, session, redirect
from model import *

deliver = Blueprint('deliver', __name__)


@deliver.route('/new', strict_slashes=False)
def new_delivery():
    od = get_orders()
    return render_template('deliverorder.html', user=session['username'], list=od)


@delivery.route('/<driver_id>/<order_id>', methods=['GET','POST'], strict_slashes=False)
def set_delivery(chef_id, kitchen_id):
    ks = get_kitchens()
    if request.method == 'POST':
        time = "5:00pm"

        if set_schedule(kitchen_id, chef_id,time):
            update_kitchen(kitchen_id[1])
            return render_template('show_schedulesuccess.html', user=session['username'])
        return "You have already scheduled this kitchen at that time, please select a different one"
    else:
        return render_template('schedulekitchen.html', user=session['username'], list=ks)
