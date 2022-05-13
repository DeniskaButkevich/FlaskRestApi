from flask import Blueprint
from flask_restx import Api

from app.controller.UserController import namespace as user_namespace
from app.main.errors import errors

blueprint = Blueprint('api', __name__, url_prefix='/api')

# Flask API Configuration
api = Api(
    blueprint,
    title='Flask RESTx API',
    version='1.0',
    description='Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation',
    doc='/doc',
    catch_all_404s=True,
    errors=errors
)

api.add_namespace(user_namespace)
