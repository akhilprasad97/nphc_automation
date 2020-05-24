import os

from flask import Flask
from flask import render_template, redirect, url_for


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def index():
        return render_template('base.html')

    from . import db
    db.init_app(app)

    from . import home
    app.register_blueprint(home.bp)

    from . import User
    app.register_blueprint(User.bp)

    from . import templates
    app.register_blueprint(templates.bp)

    return app