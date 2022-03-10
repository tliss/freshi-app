from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from auth import login_required
from models import db, User, Food

bp = Blueprint('food', __name__)

@bp.route('/')
def index():
    if g.user:
        try:
            foods=Food.query.filter_by(creator_id=g.user.id)
        except Exception as e:
            return(str(e))

        return render_template('food/index.html', foods=foods)
    else:
        return render_template('auth/login.html')

def get_food(id, check_creator=True):
    food=Food.query.filter_by(creator_id=g.user.id).first()

    if food is None:
        abort(404, f"Food id {id} doesn't exist.")

    if check_creator and food.creator_id != g.user.id:
        abort(403)

    return food

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        exp = request.form['exp']
        error = None

        if not name:
            error = 'Food name is required.'

        if error is not None:
            flash(error)
        else:
            food=Food(
                g.user.id,
                None,
                name,
                exp
            )
            db.session.add(food)
            db.session.commit()

            return redirect(url_for('food.index'))

    return render_template('food/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    food = get_food(id)

    if request.method == 'POST':
        name = request.form['name']
        exp = request.form['exp']
        error = None

        if not name:
            error = 'Food name is required.'

        if error is not None:
            flash(error)
        else:
            food.name = name
            food.expiration_date = exp
            db.session.add(food)
            db.session.commit()

            return redirect(url_for('food.index'))

    return render_template('food/update.html', food=food)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    food = get_food(id)
    db.session.delete(food)
    db.session.commit()

    return redirect(url_for('food.index'))