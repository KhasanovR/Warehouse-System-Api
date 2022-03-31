from django.urls import path, include

urlpatterns = [
        path('core/', include(('warehouse.api.core.urls', 'warehouse.core'))),
        path('account/', include(('warehouse.api.account.urls', 'warehouse.account'))),
]
