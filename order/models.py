from django.db import models
from customer.models import Customer
# Create your models here.
class Order(models.Model):
    orderDate = models.DateTimeField(verbose_name='تاریخ سفارش')
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_detail', verbose_name='سفارش دهنده')
    settlementDate = models.DateTimeField(verbose_name='تاریخ تسویه')
    description = models.TextField(verbose_name='توضیحات')
    amount = models.CharField(max_length=255, verbose_name='مبلغ کل')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    
    class Meta: 
        db_table = "orders"
        
    def __str__(self) -> str:
        return str(self.customerId)+ " " + str(self.orderDate)