from flask import Blueprint, render_template, request, session, redirect
from model import *

post = Blueprint('post', __name__)


@post.route('/', methods=['GET', 'POST'], strict_slashes=False)
def post_list_or_new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post_id = create_post(title, content, session['username'])
        info = post_information(post_id)
        return render_template('show_post.html',
                               user=session['username'],
                                info=info,
                                list_comments=comment_list(post_id))
    else:
        posts = make_list_of_dict()
        if 'username' in session:
            return render_template('home.html', user=session['username'], list=posts)
        return render_template('home.html', list=posts)

@post.route('/new', strict_slashes=False)
def post_new_form():
    return render_template('new_post.html', user=session['username'])


@post.route('/<post_id>', methods=['GET', 'POST'], strict_slashes=False)
def post_id_or_edit(post_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        update_post(post_id, title, content)
        return render_template('show_post.html',
                               user=session['username'],
                               info=post_information(post_id),
                               list_comments=comment_list(post_id))
    else:
        if 'username' in session:
            return render_template('show_post.html',
                               user=session['username'],
                               info=post_information(post_id),
                               list_comments=comment_list(post_id))
        else:
            return render_template('show_post.html',
                                   info=post_information(post_id),
                                   list_comments=comment_list(post_id))

@post.route('/<post_id>/edit', strict_slashes=False)
def post_show_edit_form(post_id):
    return render_template('edit_post.html', user=session['username'], info=post_information(post_id))


@post.route('/<post_id>/delete', methods=['POST'], strict_slashes=False)
def post_delete(post_id):
    if 'username' in session:
        delete_post_id(post_id)
        return redirect('/')
    return redirect('/')