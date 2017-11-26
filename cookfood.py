from flask import Blueprint, render_template, request, session, redirect
from model import *

post = Blueprint('post', __name__)