from flask import jsonify, make_response
from flask_restful import request
from flask_restx import Namespace, Resource, marshal_with, abort

from ..main.database import db
from ..model.product import Product as ProductModel

namespace = Namespace('product', 'CRUD product endpoints')
namespace_model = namespace.model("Products", ProductModel.resource_fields)


@namespace.marshal_list_with(namespace_model)
@namespace.route("/<int:id_product>/")
class Product(Resource):

    @marshal_with(ProductModel.resource_fields)
    def get(self, id_product):
        result = ProductModel.query.filter_by(id=id_product).first()
        if not result:
            abort(404, message="Could not find user with that id")
        return result

    @namespace.expect(namespace_model)
    @namespace.marshal_with(namespace_model)
    def patch(self, id_product):
        json_data = request.get_json()
        product = ProductModel.query.filter_by(id=id_product).first()
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

    @marshal_with(ProductModel.resource_fields)
    def delete(self, id_user):
        product = ProductModel.query.filter_by(id=id_user).first()
        if not product:
            abort(404, message="Product doesn't exist, cannot delete")
        db.session.delete(product)
        db.session.commit()
        return '', 204


@namespace.marshal_list_with(namespace_model)
@namespace.route("")
class ProductList(Resource):

    @marshal_with(ProductModel.resource_fields)
    def get(self):
        product = ProductModel.query.all()
        return product

    @namespace.expect(namespace_model)
    @namespace.marshal_with(namespace_model)
    @marshal_with(ProductModel.resource_fields)
    def put(self):
        json_data = request.get_json()
        product = ProductModel.query.filter_by(name=json_data['name']).first()
        if product:
            abort(409, message="Product name taken...")

        product = ProductModel(name=json_data['name'], description=json_data['description'], price=json_data['price'])
        db.session.add(product)
        db.session.commit()
        return product, 201

    @namespace.expect(namespace_model)
    def post(self):
        full_json_data = request.get_json()
        products = []
        for item in full_json_data:
            product = ProductModel.query.filter_by(name=item['name']).first()
            if product:
                abort(409, message="Product name taken...")

            product = ProductModel(name=item['name'], description=item['description'], price=item['price'])
            db.session.add(product)
            products.append(product)

        db.session.commit()
        data = [{'id': p.id, 'name': p.name, 'description': p.description, 'price': p.price} for p in products]
        return make_response(jsonify(data), 201)
