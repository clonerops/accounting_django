from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from .models import Order
from .serializers import OrderSerializer

# Create your views here.
class OrderConfirm(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDetail(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer