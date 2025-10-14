from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StoreViewSet, PriceViewSet, RegisterView, lowest_price
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import home, search_product

urlpatterns = [
    path('search/<str:query>/', search_product, name='search_product'),
]

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'prices', PriceViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('search/<str:query>/', search_product, name='search-product'),
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('lowest-price/<str:product_name>/', lowest_price, name='lowest-price'),
    path('search/<str:query>/', search_product, name='search_product'),
]

