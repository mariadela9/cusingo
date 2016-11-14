from flask import Flask, redirect
from user import user
from sessions import sessions
from post import post
from comments import comments

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(sessions, url_prefix='/sessions')
app.register_blueprint(post, url_prefix='/post')
app.register_blueprint(comments, url_prefix='/comments')
app.secret_key = '4.k^S:$(NhNU~(dG8/}K[~xVFjC#zx;D'


@app.route('/')
def index():
    return redirect('/post')

if __name__ == '__main__':
    app.run()