from flask import Blueprint, request, session, jsonify
from model import *

comments = Blueprint('comments', __name__)


@comments.route('/<post_id>', strict_slashes=False, methods=["POST"])
def comment_new(post_id):
    if 'username' in session:
        author = session['username']
        title = request.form['title']
        content = request.form['content']
        comment_id = new_comment(title, content, author, post_id)
        return jsonify({"title": "{}".format(title),
                        "author": "{}".format(author),
                        "content": "{}".format(content),
                        "comment_id": "{}".format(comment_id)})


@comments.route('/<comment_id>/delete', strict_slashes=False, methods=['GET', 'POST'])
def comment_delete(comment_id):
    delete_comment(comment_id)
    element_id = "comment_{}_delete".format(comment_id)
    return jsonify({'element_id': '{}'.format(element_id)})
