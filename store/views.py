from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Store
from .serializers import StoreSerializer
# Create your views here.
class StoreList(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

