from rest_framework import serializers
from .models import Order, OrderDetail

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('createdAt', 'updatedAt')

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = OrderDetail
        exclude = ('createdAt', 'updatedAt')