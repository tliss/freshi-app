from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from auth import login_required
from models import db, Post, User

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    try:
        posts=Post.query.filter_by(author_id=g.user.id)
    except Exception as e:
        return(str(e))

    return render_template('blog/index.html', posts=posts)

def get_post(id, check_author=True):
    post=Post.query.filter_by(author_id=g.user.id).first()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post.author_id != g.user.id:
        abort(403)

    return post

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post=Post(
                g.user.id,
                None,
                title,
                body
            )
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('blog.index'))