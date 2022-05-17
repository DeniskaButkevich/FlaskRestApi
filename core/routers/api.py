from flask import Blueprint
from flask_restx import Api

from core.routers.endpoints.product_endpoints import namespace as product_namespace
from core.routers.endpoints.user_endpoints import namespace as user_namespace
from core.routers.endpoints.order_endpoints import namespace as order_namespace
from core.routers.endpoints.category_endpoints import namespace as category_namespace
from core.main.errors import errors

blueprint = Blueprint('api', __name__, url_prefix='/api')

# Flask API Configuration
api = Api(
    blueprint,
    title='Flask RESTx API',
    version='1.0',
    description='Application Flask REST extension\
        for better project structure and auto generated documentation',
    doc='/doc',
    catch_all_404s=True,
    errors=errors
)

api.add_namespace(user_namespace)
api.add_namespace(product_namespace)
api.add_namespace(order_namespace)
api.add_namespace(category_namespace)
