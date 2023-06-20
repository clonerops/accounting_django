from django.urls import path
from .views import StoreList

app_name='store'
urlpatterns = [
    path('stores', StoreList.as_view(), name='store-list')
]

