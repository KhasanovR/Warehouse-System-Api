from django.urls import path
from django.views.generic import TemplateView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.schemas import get_schema_view

from warehouse.api.core.schemas import CustomOpenApiGenerator
from warehouse.tenant import admin


class IsSuperUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


urlpatterns = [
    path('admin/', admin.public_admin_site.urls),
    path(
        'api/v1/openapi/',
        get_schema_view(
            generator_class=CustomOpenApiGenerator,
            title='Warehouse API',
            description='Warehouse API',
            version='0.0.6',
            urlconf='warehouse.api.urls.v1',
            permission_classes=[IsSuperUser],
            authentication_classes=[BasicAuthentication, SessionAuthentication],
            url='/api/v1/',
        ),
        name='openapi-schema-v1'
    ),
    path('api/v1/docs/', TemplateView.as_view(
        template_name='docs/redoc.html',
        extra_context={'schema_url': 'openapi-schema-v1'}
    ), name='docs-v1')

]
