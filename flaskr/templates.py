import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db
bp = Blueprint('templates', __name__, url_prefix='/templates')
@bp.route('/create', methods=('GET', 'POST'))
def create():
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT Template_Id FROM TEMPLATE_S')
    rows = cur.fetchall()
    templates=[]
    for row in rows:
        templates.append(row['Template_Id'])

    if request.method == 'POST':
        customer = request.form['customer']
        template = request.form['template']
        description = request.form['description']
        db = get_db()
        if template in templates:
            flash('template name already exists')
            return redirect(url_for('templates.create'))
        db.execute(
            'insert into TEMPLATE_S (Customer_name, Template_Id, Description_) VALUES (?, ?, ?)', (customer, template, description)
        )
        db.commit()
        return redirect(url_for('home.index'))
    return render_template('template/create.html')

@bp.route('/vet', methods=('GET', 'POST'))
def vet():
    if request.method == 'POST':
        custmoer = request.form['Custmoer']
        db = get_db()
        
        return redirect(url_for('/home'))

    return render_template('template/view_edit.html', customers = ['ram', 'adi', 'aditya'], commands = ['show', 'show process', 'show run'])

@bp.route('/view', methods=('GET', 'POST'))
def view():
    return render_template('template/view.html', customers = ['ram', 'adi', 'aditya'], templates = ['show', 'show process', 'show run'])

