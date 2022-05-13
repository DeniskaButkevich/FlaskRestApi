from flask import jsonify, make_response
from flask_restful import request
from flask_restx import Namespace, Resource, marshal_with, abort

from ..main.database import db
from ..model.user import User as UserModel

namespace = Namespace('User', 'CRUD user endpoints')
namespace_model = namespace.model("User", UserModel.resource_fields)


@namespace.marshal_list_with(namespace_model)
@namespace.route("/users/<int:id_user>/")
class User(Resource):

    @marshal_with(UserModel.resource_fields)
    def get(self, id_user):
        result = UserModel.query.filter_by(id=id_user).first()
        if not result:
            abort(404, message="Could not find user with that id")
        return result

    @marshal_with(UserModel.resource_fields)
    def put(self, id_user):
        json_data = request.get_json()
        result = UserModel.query.filter_by(id=id_user).first()
        if result:
            abort(409, message="User id taken...")

        video = UserModel(id=json_data['id'], fullname=json_data['fullname'], username=json_data['username'],
                          password=json_data['password'], email=json_data['email'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(UserModel.resource_fields)
    def patch(self, id_user):
        json_data = request.get_json()
        result = UserModel.query.filter_by(id=id_user).first()
        if not result:
            abort(404, message="User doesn't exist, cannot update")

        if json_data['fullname']:
            result.fullname = json_data['fullname']

        db.session.commit()

        return result

    @marshal_with(UserModel.resource_fields)
    def delete(self, id_user):
        result = UserModel.query.filter_by(id=id_user).first()
        if not result:
            abort(404, message="User doesn't exist, cannot delete")
        db.session.delete(result)
        db.session.commit()
        return '', 204


@namespace.route("/users/")
class UserList(Resource):

    @marshal_with(UserModel.resource_fields)
    def get(self):
        result = UserModel.query.all()
        return result

    @marshal_with(UserModel.resource_fields)
    def post(self):
        full_json_data = request.get_json()
        users = []
        for x in full_json_data:

            result = UserModel.query.filter_by(id=x['id']).first()
            if result:
                abort(409, message="User id taken...")

            user = UserModel(id=x['id'], fullname=x['fullname'], username=x['username'],
                             password=x['password'], email=x['email'])
            db.session.add(user)
            users.append(user)

        db.session.commit()
        data = [{'id': p.id, 'fullname': p.fullname, 'password': p.password} for p in users]
        return make_response(jsonify(data), 201)
