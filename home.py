from flask import Flask, redirect
from customer import customer
from sessions import sessions
from post import post
from comments import comments
from driver import driver
from chef import chef
from schedulekitchen import kitchen
from admin import admin
from offerorder import offer
from placeorder import order
from deliver import deliver

app = Flask(__name__)
app.register_blueprint(deliver, url_prefix='/deliver')
app.register_blueprint(order, url_prefix='/order')
app.register_blueprint(customer, url_prefix='/customer')
app.register_blueprint(offer, url_prefix='/offer')
app.register_blueprint(chef, url_prefix='/chef')
app.register_blueprint(driver, url_prefix='/driver')
app.register_blueprint(sessions, url_prefix='/sessions')
app.register_blueprint(post, url_prefix='/post')
app.register_blueprint(comments, url_prefix='/comments')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(kitchen, url_prefix='/kitchen')
# app.register_blueprint(order, url_prefix='/kitchen')
app.secret_key = '4.k^S:$(NhNU~(dG8/}K[~xVFjC#zx;D'


@app.route('/')
def index():
    return redirect('/post')

if __name__ == '__main__':
    app.debug = True
    app.run()
