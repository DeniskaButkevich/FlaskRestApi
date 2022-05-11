from flask_restful import Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# from app.model.user import User as UserModel

db = SQLAlchemy()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("fullname", type=str, help="fullname of the user is required", required=True)
video_put_args.add_argument("username", type=str, help="username of the user is required", required=True)
video_put_args.add_argument("password", type=str, help="password of the user is required", required=True)
video_put_args.add_argument("email", type=str, help="email of the user is required", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("fullname", type=str, help="fullname of the user is required")

resource_fields = {
    'id': fields.Integer,
    'fullname': fields.String,
    'username': fields.String,
    'password': fields.String,
    'email': fields.String
}


@marshal_with(resource_fields)
def get(self, id_user):
    # result = UserModel.query.filter_by(id=id_user).first()
    # if not result:
    #     abort(404, message="Could not find user with that id")
    # return result
    pass


@marshal_with(resource_fields)
def put(self, id_user):
    # args = video_put_args.parse_args()
    # result = UserModel.query.filter_by(id=id_user).first()
    # if result:
    #     abort(409, message="User id taken...")
    #
    # video = UserModel(id=id_user, fullname=args['fullname'], username=args['username'], password=args['password'],
    #                   email=args['email'])
    # db.session.add(video)
    # db.session.commit()
    # return video, 201
    pass


@marshal_with(resource_fields)
def patch(self, id_user):
    # args = video_update_args.parse_args()
    # result = UserModel.query.filter_by(id=id_user).first()
    # if not result:
    #     abort(404, message="User doesn't exist, cannot update")
    #
    # if args['fullname']:
    #     result.name = args['name']
    #
    # db.session.commit()
    #
    # return result
    pass


@marshal_with(resource_fields)
def delete(self, id_user):
    # abort(404, message="User doesn't exist, cannot update")
    # # del videos[video_id]
    # return '', 204
    pass


class UserList(Resource):

    def get(self):
        pass

    def post(self):
        pass
