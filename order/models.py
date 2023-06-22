from django.db import models
from customer.models import Customer
from product.models import Product
from store.models import Store
# Create your models here.
class Order(models.Model):
    orderDate = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')
    # orderId = models.ManyToManyField('self', default=0, verbose_name="شناسه سفرش")
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_detail', verbose_name='سفارش دهنده')
    settlementDate = models.DateTimeField(verbose_name='تاریخ تسویه')
    description = models.TextField(verbose_name='توضیحات')
    amount = models.CharField(max_length=255, verbose_name='مبلغ کل')
    isPayment = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    
    class Meta: 
        db_table = "orders"
        
    def __str__(self) -> str:
        return str(self.customerId)+ " " + str(self.orderDate)

class OrderDetail(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_detail', verbose_name="شناسه سفارش")
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_detail', verbose_name="شناسه محصول")
    storeId = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="store_detail", verbose_name="شناسه انبار")
    amount = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta: 
        db_table = "orders_detail"
        
    def __str__(self) -> str:
        return str(self.orderId)
