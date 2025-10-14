from rest_framework import serializers
from .models import Product, Store, Price
from .models import Product, PriceHistory
from django.contrib.auth.models import User


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
class PriceHistorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = PriceHistory
        fields = ['id', 'product', 'price', 'date']
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
