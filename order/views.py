from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer

# Create your views here.
class OrderConfirm(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class CrateOrderDetail(CreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

class OrderDetail(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer