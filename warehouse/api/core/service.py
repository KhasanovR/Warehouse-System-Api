from warehouse.core.models import Product
from warehouse.api.core.serializers import (
    OutputSerializer,
)


class Service:
    @staticmethod
    def process(data):
        serializer = OutputSerializer()
        result_serializer = serializer.ResultSerializer()
        product_material_serializer = result_serializer.ProductMaterialSerializer()

        for element in data:
            product = Product.objects.get(id=element["product"].id)
            result_serializer.data["product_name"] = product.name
            result_serializer.data["product_qty"] = element["quanity"]

            for product_material in product.product_materials:
                material = product_material.material
                required_quantiy = product_material.quanity * element["quanity"]
                for warehouse in material.warehouses:
                    product_material_serializer.data["material_name"] = material.name
                    product_material_serializer.data["qty"] = warehouse.reminder

                    if required_quantiy > warehouse.reminder:
                        required_quantiy -= warehouse.reminder
                        product_material_serializer.data["warehouse_id"] = warehouse.id
                        product_material_serializer.data["price"] = warehouse.price
                    else:
                        product_material_serializer.data["qty"] = None
                result_serializer.data["product_materials"] = product_material_serializer.data
            serializer.data["result"] = result_serializer.data

        return serializer.data
