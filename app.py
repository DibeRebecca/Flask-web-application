from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Rebecca World!</p>"

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



@app.route("/<name>")
def hellos(name):
    return f"Hello, {escape(name)}!"
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
url_for('static', filename='style.css')


