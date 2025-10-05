from rest_framework import serializers
from .models import Product, Store, Price

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    store = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Price
        fields = '__all__'
