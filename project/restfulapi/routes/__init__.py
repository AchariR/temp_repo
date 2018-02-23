from flask import Blueprint
import flask_restful
from setuptools import find_packages
from project import app
import project.restfulapi.routes.route_decorator

def get_blueprints(blueprints, filter_path=''):
    paths = []
    for path in find_packages():
        if filter_path in path:
            paths.append(path)
    for path in paths:
        blueprints[path] = Blueprint(path, path)
    for path in paths:
        __import__(path)
        app.register_blueprint(blueprints[path])