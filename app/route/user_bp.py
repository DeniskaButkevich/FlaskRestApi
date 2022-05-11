from flask import Blueprint

from ..controller.UserController import get, put, patch, delete

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/<int:user_id>', methods=['GET'])(get)
user_bp.route('/create', methods=['POST'])(put)
user_bp.route('/<int:user_id>/edit', methods=['POST'])(patch)
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete)