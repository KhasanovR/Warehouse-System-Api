from django.contrib import admin
from reversion.admin import VersionAdmin

from warehouse.core.models import (
    Product,
    Material,
    ProductMaterial,
)


@admin.register(Product)
class ProductAdmin(VersionAdmin):
    list_display = [
        'name',
        'code',
    ]
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'name',
                    'code',
                ]
            }
        ),
    ]
    list_filter = []
    search_fields = [
        'name',
        'code'
    ]

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Material)
class MaterialAdmin(VersionAdmin):
    list_display = [
        'name',
    ]
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'name',
                ]
            }
        ),
    ]
    list_filter = []
    search_fields = [
        'name'
    ]

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(ProductMaterial)
class ProductMaterialAdmin(VersionAdmin):
    list_display = [
        'product',
        'material',
        'quantity',
    ]
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'product',
                    'material',
                    'quantity',
                ]
            }
        ),
    ]
    list_filter = []
    search_fields = [
        'product',
        'material',
    ]

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
