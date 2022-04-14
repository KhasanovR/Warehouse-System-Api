from warehouse.core.models import Product
from warehouse.api.v1.core.serializers import (
    OutputSerializer,
)


class Service:
    @staticmethod
    def process(data):
        result = {'result': []}

        for element in data:
            product = Product.objects.get(id=element["product"].id)
            outter_temp = {"product_name": product.name, "product_qty": element["quanity"], "product_materials": []}
            for product_material in product.product_materials:
                material = product_material.material
                required_quantiy = product_material.quanity * element["quanity"]
                for warehouse in material.warehouses:
                    inner_temp = {"material_name": material.name, "qty": warehouse.reminder}

                    if required_quantiy > warehouse.reminder:
                        required_quantiy -= warehouse.reminder
                        inner_temp["warehouse_id"] = warehouse.id
                        inner_temp["price"] = warehouse.price
                    else:
                        inner_temp["warehouse_id"] = None
                        inner_temp["price"] = None
                outter_temp["product_materials"].append(inner_temp)
            result["result"].append(outter_temp)
        serializer = OutputSerializer(data=result, many=True)
        serializer.is_valid()
        return serializer.validated_data
