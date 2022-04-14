from django.urls import path, include

urlpatterns = [
        path('core/', include('warehouse.api.v1.core.urls')),
        path('account/', include('warehouse.api.v1.account.urls')),
]
