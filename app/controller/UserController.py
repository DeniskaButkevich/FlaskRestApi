from flask import jsonify, make_response, request
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
        result = UserModel.query.filter_by(id=id_user).first()
        if not result:
            abort(404, message="Could not find user with that id")
        return result

    @namespace.expect(namespace_model)
    @namespace.marshal_with(namespace_model)
    def patch(self, id_user):
        json_data = request.get_json()
        result = UserModel.query.filter_by(id=id_user).first()
        if not result:
            abort(404, message="User doesn't exist, cannot update")

        if json_data['fullname']:
            result.fullname = json_data['fullname']

        db.session.commit()

        return result

    @namespace.marshal_with(namespace_model)
    def delete(self, id_user):
        result = UserModel.query.filter_by(id=id_user).first()
        if not result:
            abort(404, message="User doesn't exist, cannot delete")
        db.session.delete(result)
        db.session.commit()
        return '', 204


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

    @namespace.expect(namespace_model)
    def post(self):
        full_json_data = request.get_json()
        users = []
        for item in full_json_data:

            user = UserModel.query.filter_by(id=item['id']).first()
            if user:
                abort(409, message="User id taken...")

            user = UserModel(fullname=item['fullname'], username=item['username'],
                             password=item['password'], email=item['email'])
            db.session.add(user)
            users.append(user)

        db.session.commit()
        data = [{'id': u.id, 'fullname': u.fullname, 'password': u.password} for u in users]
        return make_response(jsonify(data), 201)
