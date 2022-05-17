from flask import request
from flask_restx import Resource, abort

from core.main.database import db
from core.model.product import Product as Model, model, model_update, namespace


@namespace.route("/<int:id_product>/")
class Product(Resource):

    @namespace.marshal_with(model)
    def get(self, id_product):
        product = Model.query.filter_by(id=id_product).first()
        return product if product else abort(404, message="Could not find user with that id")

    @namespace.expect(model_update)
    @namespace.marshal_with(model)
    def patch(self, id_product):
        json_data = request.get_json()
        product = Model.query.filter_by(id=id_product).first()
        if not product:
            abort(404, message="Product doesn't exist, cannot update")

        if json_data['name']:
            product.description = json_data['name']
        if json_data['description']:
            product.description = json_data['description']
        if json_data['price']:
            product.price = json_data['price']

        db.session.commit()
        return product

    @namespace.marshal_with(model)
    def delete(self, id_user):
        product = Model.query.filter_by(id=id_user).first()
        if not product:
            abort(404, message="Product doesn't exist, cannot delete")
        db.session.delete(product)
        db.session.commit()
        return '', 204


@namespace.route("")
class ProductList(Resource):

    @namespace.marshal_with(model)
    def get(self):
        aaa = Model.query.all()
        return aaa

    @namespace.expect(model_update)
    @namespace.marshal_with(model)
    def put(self):
        json_data = request.get_json()
        self.if_exist_product(json_data)

        product = Model(name=json_data['name'], description=json_data['description'], price=json_data['price'])
        db.session.add(product)
        db.session.commit()
        return product, 201

    @namespace.expect([model_update])
    @namespace.marshal_with(model)
    def post(self):
        full_json_data = request.get_json()
        products = []
        for item in full_json_data:
            self.if_exist_product(item)

            product = Model(name=item['name'], description=item['description'], price=item['price'])
            db.session.add(product)
            products.append(product)

        db.session.commit()
        return products

    @staticmethod
    def if_exist_product(json_data):
        product = Model.query.filter_by(name=json_data['name']).first()
        if product:
            abort(409, message="Product name taken...")
