from rest_framework import serializers
from .models import Product
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'nationalCode')

class ProductSerializer(serializers.ModelSerializer):
    createdBy = UserSerializer()
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'isStock', 'createdBy')