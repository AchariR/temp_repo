import project.restfulapi.session
from project.restfulapi.routes import get_blueprints

blueprints = {}
get_blueprints(blueprints, 'project.restfulapi.')