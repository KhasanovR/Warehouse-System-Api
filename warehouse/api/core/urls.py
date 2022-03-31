from rest_framework.routers import SimpleRouter

from warehouse.api.core.views import (
    ResultViewSet,
)

router = SimpleRouter()

router.register(r'results', ResultViewSet, basename='results')

urlpatterns = router.urls
