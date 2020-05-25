import functools
import pymongo

from collections import defaultdict
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.utils import secure_filename
from flaskr.db import get_mongo

bp = Blueprint('home', __name__, url_prefix='/home')
@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        customer = request.form['customer']
        template = request.form['template']
        input_file = request.files['file']
        input_file.save(secure_filename(input_file.filename))
        print("The customer name is '" + customer + "'")

    return render_template('home.html')



    



   
    
    