import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .mongod import create_template
bp = Blueprint('extra', __name__, url_prefix='/extra')
@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        customer = request.form['customer']
        template = request.form['template']
        description = request.form['description']
        create_template(customer,template,description)
        '''template_collection = mongo.db.templates
        template_collection.insert({'customer':customer, 'template':template, 'description':description})'''
        return redirect(url_for('home.index'))

    return render_template('extra.html', customers = ['ram', 'adi', 'aditya'], commands = ['show', 'show process', 'show run'])

