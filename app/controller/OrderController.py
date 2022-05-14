from flask_restx import Namespace, Resource

from ..model.order import Order as OrderModel

namespace = Namespace('order', 'CRUD order endpoints')
namespace_model = namespace.model("Order", OrderModel.resource_fields)


@namespace.marshal_list_with(namespace_model)
@namespace.route("/<int:id_order>/")
class Order(Resource):

    def get(self, id_order):
        pass

    def patch(self, id_order):
        pass

    def delete(self, id_order):
        pass


@namespace.marshal_list_with(namespace_model)
@namespace.route("")
class OrderList(Resource):

    def get(self):
        pass

    def put(self):
        pass

