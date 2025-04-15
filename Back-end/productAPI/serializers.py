from rest_framework import serializers
from .models import Product, Order, OrderItem
from .models import Cart, CartItem

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # default is True

    class Meta:
        model = Product 
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False}  ,
            'price':{'min_value': 0},
            'stock':{'min_value': 0},
        }
    def validate_price(self, value):
        if value > 0:
            return value
        else:
            raise serializers.ValidationError("Price must be greater than 0")

  
class OrderSerializer(serializers.ModelSerializer):
    product= serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = Order
        fields = '__all__'
class OrderItemSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = OrderItem
        fields = '__all__'
        extra_kwargs = {
            'quantity': {'min_value': 1},
        }
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'items']