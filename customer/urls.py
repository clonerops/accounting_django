from django.urls import path
from .views import CustomerCreate, CustomerList, CustomerDetail

app_name='customer'
urlpatterns = [
    path('customers/create', CustomerCreate.as_view(), name='customer-create'),
    path('customers', CustomerList.as_view(), name='customer-lists'),
    path('customers/<int:pk>', CustomerDetail.as_view(), name='customer-detail')
]