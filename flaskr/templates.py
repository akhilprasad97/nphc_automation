import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_mongo
bp = Blueprint('templates', __name__, url_prefix='/templates')
@bp.route('/create', methods=('GET', 'POST'))
def create():
    mongo = get_mongo()
    db_name = mongo["temp_ASR9K"]
    list_show_commands = list(map(lambda x: x.replace("_", " "), db_name.list_collection_names()))
    print(list_show_commands)

    if request.method == 'POST':
        customer = request.form['customer']
        template = request.form['template']
        description = request.form['description']
        
        return redirect(url_for('home.index'))
    return render_template('template/create.html',commands=list_show_commands)


    

@bp.route('/vet', methods=('GET', 'POST'))
def vet():
    if request.method == 'POST':
        custmoer = request.form['Custmoer']
       
        
        return redirect(url_for('/home'))

    return render_template('template/view_edit.html', customers = ['ram', 'adi', 'aditya'], commands = ['show', 'show process', 'show run'])

@bp.route('/view', methods=('GET', 'POST'))
def view():
    return render_template('template/view.html', customers = ['ram', 'adi', 'aditya'], templates = ['show', 'show process', 'show run'])

