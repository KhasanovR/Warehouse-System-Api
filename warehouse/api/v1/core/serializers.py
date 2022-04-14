from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from warehouse.core.models import (
    Product,
    Material,
    ProductMaterial,
    Warehouse
)


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=255)
    code = serializers.CharField(max_length=255, validators=[UniqueValidator(queryset=Product.objects.all())])

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'code',
        ]


class MaterialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Material
        fields = [
            'id',
            'name',
        ]


class ProductMaterialSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    material = MaterialSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = ProductMaterial
        fields = [
            'product',
            'material',
            'quantity',
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    reminder = serializers.IntegerField()
    price = serializers.DecimalField(decimal_places=2, max_digits=12)


class Meta:
    model = Warehouse
    fields = [
        'material',
        'reminder',
        'price',
    ]


class InputSerializer(serializers.Serializer):
    product = ProductSerializer()
    quanity = serializers.IntegerField()


class OutputSerializer(serializers.Serializer):
    class ProductMaterialSerializer(serializers.Serializer):
        warehouse_id = serializers.IntegerField()
        material_name = serializers.CharField(max_length=255)
        qty = serializers.IntegerField()
        price = serializers.DecimalField(decimal_places=2, max_digits=12)

    product_name = serializers.CharField(max_length=255)
    product_qty = serializers.IntegerField()
    product_materials = ProductMaterialSerializer(many=True)

