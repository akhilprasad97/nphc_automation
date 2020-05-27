import functools
import pymongo

from collections import defaultdict
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.utils import secure_filename
from flaskr.db import get_mongo

bp = Blueprint('ajax_reqs', __name__, url_prefix='/ajax_reqs')

@bp.route('/select_template', methods=["GET"])
def select_template():
    cust = request.args.get('customer')
    print(cust)
    mongo = get_mongo()
    templates = mongo["temp_UI"]["templates"].find({"customer" : cust})
    templates_send = "<option value="" disabled=true selected=true>Select Template</option>"
    for temp in templates:
        templates_send = templates_send + "<option value=\"" + str(temp["template_name"]) + "\">" + str(temp["template_name"]) + "</option>"
    print(templates_send)
    return templates_send