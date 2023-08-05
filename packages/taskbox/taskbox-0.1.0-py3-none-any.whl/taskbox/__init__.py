#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from os import makedirs

from flask import Flask

from taskbox.auth import auth
from taskbox.api import api
from taskbox.db import init_app
from taskbox.run import run
from taskbox.manage import manage
from taskbox.token import token


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=path.join(app.instance_path, "taskbox.sqlite"),
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)
    try:
        makedirs(app.instance_path)
    except OSError:
        pass
    init_app(app)
    app.register_blueprint(auth)
    app.register_blueprint(api)
    app.register_blueprint(manage)
    app.register_blueprint(run)
    app.register_blueprint(token)
    app.add_url_rule("/", endpoint="index")
    return app
