from django.urls import path
from .views import OrderConfirm, OrderDetail, OrderList

app_name='order'
urlpatterns = [
    path('orders/create', OrderConfirm.as_view(), name='order-create'),
    path('orders', OrderList.as_view(), name='order-lists'),
    path('orders/<int:pk>', OrderDetail.as_view(), name='order-detail')
]