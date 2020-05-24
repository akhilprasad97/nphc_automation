import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_mongo

bp = Blueprint('User', __name__, url_prefix='/User')
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_mongo()
        error = None

        if username is None:
            error = 'Select a customer'
        elif password:
            error = 'Select a command'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('/home/caj'))

        flash(error)

    return render_template('User/login.html')