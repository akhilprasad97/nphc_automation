import functools
from collections import defaultdict
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db
bp = Blueprint('home', __name__, url_prefix='/home')
@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        customer = request.form['customer']
        template = request.form['template']
        db = get_db()
        db = get_db()
        db.execute(
            'insert into JOB_S (Customer_name, Template_Id) VALUES (?, ?)', (customer, template)
        )
        db.commit()
        return redirect(url_for('home.index'))

    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT Customer_name, Template_Id FROM TEMPLATE_S')
    rows = cur.fetchall()
    customers=[row['Customer_name'] for row in rows]
    templates=[row['Template_Id'] for row in rows]
    return render_template('home.html', customers = customers , templates = templates)

