from rest_framework.routers import SimpleRouter

from warehouse.api.v1.core.views import (
    ResultViewSet,
)

router = SimpleRouter()
router.register(r'users', ResultViewSet, basename="users")

urlpatterns = []

urlpatterns += router.urls
