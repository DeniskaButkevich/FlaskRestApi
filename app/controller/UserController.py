from flask import jsonify, make_response
from flask_restful import Resource, reqparse, marshal_with, abort, request

from ..main.database import db
from ..model.user import User as UserModel

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("id", type=int, help="id of the user is required", required=True)
video_put_args.add_argument("fullname", type=str, help="fullname of the user is required", required=True)
video_put_args.add_argument("username", type=str, help="username of the user is required", required=True)
video_put_args.add_argument("password", type=str, help="password of the user is required", required=True)
video_put_args.add_argument("email", type=str, help="email of the user is required", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("fullname", type=str, help="fullname of the user is required")


class User(Resource):

    @marshal_with(UserModel.resource_fields)
    def get(self, id_user):
        result = UserModel.query.filter_by(id=id_user).first()
        if not result:
            abort(404, message="Could not find user with that id")
        return result

    @marshal_with(UserModel.resource_fields)
    def put(self, id_user):
        args = video_put_args.parse_args()
        result = UserModel.query.filter_by(id=id_user).first()
        if result:
            abort(409, message="User id taken...")

        video = UserModel(id=args['id'], fullname=args['fullname'], username=args['username'],
                          password=args['password'], email=args['email'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(UserModel.resource_fields)
    def patch(self, id_user):
        args = video_update_args.parse_args()
        result = UserModel.query.filter_by(id=id_user).first()
        if not result:
            abort(404, message="User doesn't exist, cannot update")

        if args['fullname']:
            result.fullname = args['fullname']

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
