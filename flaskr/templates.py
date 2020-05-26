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

    if request.method == 'POST':
        form_data = request.form
        push_template = {}
        push_template["customer"] = form_data.get("customer")
        push_template["template_name"] = request.form['template']
        push_template["desc"] = request.form['desc']
        push_template["os"] = request.form['ostype']
        push_template["platform"] = request.form['platform']
        push_template["commands"] = request.form.getlist('commands')
        db_ui = mongo["temp_UI"]
        template_coll = db_ui["templates"]
        template_coll.insert_one(push_template)
        
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

