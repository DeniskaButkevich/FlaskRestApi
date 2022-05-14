from flask import request
from flask_restx import Namespace, Resource, abort

from ..main.database import db
from ..model.user import User as UserModel

namespace = Namespace('users', 'CRUD user endpoints')
namespace_model = namespace.model("User", UserModel.resource_fields)


@namespace.marshal_list_with(namespace_model)
@namespace.route("/<int:id_user>/")
class User(Resource):

    @namespace.marshal_with(namespace_model)
    def get(self, id_user):
        return self.if_exist_user(id_user)

    @namespace.expect(namespace_model)
    @namespace.marshal_with(namespace_model)
    def patch(self, id_user):
        json_data = request.get_json()
        user = self.if_exist_user(id_user)

        if json_data['fullname']:
            user.fullname = json_data['fullname']
        db.session.commit()
        return user

    @namespace.marshal_with(namespace_model)
    def delete(self, id_user):
        user = self.if_exist_user(id_user)
        db.session.delete(user)
        db.session.commit()
        return '', 204

    @staticmethod
    def if_exist_user(id_user):
        user = UserModel.query.filter_by(id=id_user).first()
        if not user:
            abort(404, message="Could not find user with that id")
        return user


@namespace.marshal_list_with(namespace_model)
@namespace.route("")
class UserList(Resource):

    @namespace.marshal_with(namespace_model)
    def get(self):
        result = UserModel.query.all()
        return result

    @namespace.expect(namespace_model)
    @namespace.marshal_with(namespace_model)
    def put(self):
        json_data = request.get_json()

        user = UserModel.query.filter_by(id=json_data['id']).first()
        if user:
            abort(409, message="User id taken...")

        user = UserModel(fullname=json_data['fullname'], username=json_data['username'],
                         password=json_data['password'], email=json_data['email'])
        db.session.add(user)
        db.session.commit()
        return user, 201
