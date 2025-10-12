from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StoreViewSet, PriceViewSet
from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    PriceHistoryListCreateView, PriceHistoryDetailView
)

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'prices', PriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
