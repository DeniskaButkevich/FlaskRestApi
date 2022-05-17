from flask import request
from flask_restx import Resource, abort

from core.model.order import Order as Model, model, model_patch, model_put, namespace
from core.main.database import db
from core.model.product import Product as ProductModel
from core.model.user import User as UserModel


@namespace.route("/<int:id_order>/")
class Order(Resource):

    @namespace.marshal_with(model)
    def get(self, id_order):
        order = Model.query.filter_by(id=id_order).first()
        return order if order else abort(404, message="Could not find order with that id")

    @namespace.expect(model_patch)
    @namespace.marshal_with(model)
    def patch(self, id_order):
        json_data = request.get_json()
        order = Model.query.filter_by(id=id_order).first()
        if not order:
            abort(404, message="Order doesn't exist, cannot update")

        if json_data['status']:
            order.status = json_data['status']

        db.session.commit()
        return order

    @staticmethod
    def delete(id_order):
        order = Model.query.filter_by(id=id_order).first()
        if not order:
            abort(404, message="Order doesn't exist, cannot delete")
        db.session.delete(order)
        db.session.commit()
        return '', 204


@namespace.route("")
class OrderList(Resource):

    @namespace.marshal_with(model)
    def get(self):
        return Model.query.all()

    @namespace.expect(model_put)
    @namespace.marshal_with(model)
    def put(self):
        json_data = request.get_json()
        products_f = []
        pp = ProductModel.query.filter_by(id=json_data['products']['id']).first()
        uu = UserModel.query.filter_by(id=json_data['user']['id']).first()
        products_f.append(pp)
        order = Model(address=json_data['address'], products=products_f, user=uu)
        db.session.add(order)
        db.session.commit()
        return order, 201
