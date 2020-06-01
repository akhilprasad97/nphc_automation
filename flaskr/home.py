import functools
import os
import pymongo
from flaskr.NewFile import createFolder

from collections import defaultdict
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.utils import secure_filename
from flaskr.db import get_mongo
from datetime import datetime

# datetime object containing current date and time




bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/', methods=('GET', 'POST'))
def index():
    scriptPath = os.path.dirname(os.path.realpath(__file__))
    mongo = get_mongo()
    template_coll = mongo["temp_UI"]["templates"]
    templates = template_coll.find()
    temp_coll = {}
    
    if request.method == 'POST':
        customer = request.form['customer']
        template = request.form['template']
        input_file = request.files['file']
        now = datetime.now()
        for temp in templates:
            if temp['customer'] == customer:
                platformName = temp['platform']
        input_file.save(secure_filename(input_file.filename))
        createFolder(customer,platformName,scriptPath,now)
        print("The customer name is '" + customer + "'")

    for temp in templates:
        if temp["customer"] in temp_coll:
            temp_coll[temp["customer"]].append(temp["template_name"])
            continue
        temp_coll[temp["customer"]] = [temp["template_name"]]
    print(temp_coll)

    return render_template('home.html', template_customer=temp_coll)