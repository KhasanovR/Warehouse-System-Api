from django.urls import path
from rest_framework.routers import SimpleRouter

from warehouse.api.v1.account.views import TokenObtainPairView, TokenRefreshView, UserViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet, basename="users")

urlpatterns = [
    path('me/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
