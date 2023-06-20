from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .seralizers import CustomerSerializer
from .models import Customer
# Create your views here.
class CustomerCreate(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerList(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerDetail(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer