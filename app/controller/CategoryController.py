from flask import request
from flask_restx import Namespace, Resource, abort, marshal_with, fields

from ..model.category import Category as CategoryModel
from ..model.product import Product as ProductModel
from ..main.database import db

namespace = Namespace('category', 'CRUD category endpoints')
namespace_model = namespace.model("Categories", CategoryModel.resource_fields)
namespace_model_update = namespace.model("CategoriesUpdate", CategoryModel.update_fields)


@namespace.route("/<int:id_category>/")
class Category(Resource):

    @namespace.marshal_with(namespace_model)
    def get(self, id_category):
        category = CategoryModel.query.filter_by(id=id_category).first()
        return category if category else abort(404, message="Could not find user with that id")

    @namespace.expect(namespace_model_update)
    @namespace.marshal_with(namespace_model)
    def patch(self, id_category):
        json_data = request.get_json()

        category = CategoryModel.query.filter_by(id=id_category).first()
        if not category:
            abort(404, message="Category doesn't exist, cannot update")

        if json_data['name']:
            category.name = json_data['name']

        db.session.commit()
        return category

    @namespace.marshal_with(namespace_model)
    def delete(self, id_category):
        category = CategoryModel.query.filter_by(id=id_category).first()
        if not category:
            abort(404, message="Category doesn't exist, cannot delete")
        db.session.delete(category)
        db.session.commit()
        return '', 204


@namespace.route("")
class CategoryList(Resource):

    @namespace.marshal_with(namespace_model)
    def get(self):
        return CategoryModel.query.all()

    @namespace.expect(namespace_model_update)
    @namespace.marshal_with(namespace_model)
    def put(self):
        json_data = request.get_json()
        category = CategoryModel.query.filter_by(name=json_data['name']).first()
        if category:
            abort(409, message="Category name taken...")

        category = CategoryModel(name=json_data['name'])
        db.session.add(category)
        db.session.commit()
        return category, 201


@namespace.route("/<int:id_category>/product/<int:id_product>")
class CategoryProduct(Resource):

    @namespace.marshal_with(namespace_model)
    def patch(self, id_category, id_product):
        category = CategoryModel.query.filter_by(id=id_category).first()
        product = ProductModel.query.filter_by(id=id_product).first()
        if not category or not product:
            abort(409, message="Category or Product not found...")
        category.products.append(product)
        db.session.commit()
        return category

    @staticmethod
    def delete(id_category, id_product):
        category = CategoryModel.query.filter_by(id=id_category).first()
        product = ProductModel.query.filter_by(id=id_product).first()
        if category or product:
            abort(409, message="Category or Product not found...")
        category.products.remove(product)
        db.session.commit()
        return '', 201

