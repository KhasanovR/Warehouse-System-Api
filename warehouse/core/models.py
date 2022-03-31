import reversion
from django.db import models


@reversion.register()
class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return "{}:{}".format(self.code, self.name)

    class Meta:
        db_table = 'products'


@reversion.register()
class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return '{}:{}'.format(self.id, self.name)

    class Meta:
        db_table = 'materials'


@reversion.register()
class ProductMaterial(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='product_materials',
        on_delete=models.PROTECT,
    )
    material = models.ForeignKey(
        Material,
        related_name='product_materials',
        on_delete=models.PROTECT,
    )
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return "{'product': {}, 'material': {}}".format(self.product_id, self.raw_material_id)

    class Meta:
        db_table = 'product_materials'
        unique_together = (
            'product',
            'material'
        )


@reversion.register()
class Warehouse(models.Model):
    material = models.ForeignKey(
        Material,
        related_name='warehouses',
        on_delete=models.PROTECT,
    )
    reminder = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=None,
    )

    def __str__(self) -> str:
        return 'Material ID:{}'.format(self.id)

    class Meta:
        db_table = 'warehouses'
