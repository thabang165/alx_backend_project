from rest_framework import viewsets
from .models import Product, Store, Price, PriceHistory
from .serializers import ProductSerializer, StoreSerializer, PriceSerializer, PriceHistorySerializer
from rest_framework import generics
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ProductSerializer, PriceHistorySerializer
from .models import Product, PriceHistory
# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Price
from .serializers import PriceSerializer

@api_view(['GET'])
def lowest_price(request, product_name):
    try:
        product = Product.objects.get(name__iexact=product_name)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

    prices = Price.objects.filter(product=product).order_by('amount')
    if not prices.exists():
        return Response({"message": "No prices available for this product"}, status=404)

    serializer = PriceSerializer(prices.first())
    return Response(serializer.data)


# existing views above...

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# PriceHistory
class PriceHistoryListCreateView(generics.ListCreateAPIView):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

class PriceHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
