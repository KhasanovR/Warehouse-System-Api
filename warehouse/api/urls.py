from django.urls import path, include

urlpatterns = [
        path('v1/', include('warehouse.api.v1.urls')),
]
