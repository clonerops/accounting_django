from django.db import models
from account.models import User
# Create your models here.
class ProductGroup(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان")
    description = models.TextField(blank=True, null=True,verbose_name="توضیحات")
    isDeleted = models.BooleanField(default=False, verbose_name="آیا محصول در لیست حذف شده ها باشد؟")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    
    class Meta:
        db_table = "productgroups"
        verbose_name="گروه محصول"
        verbose_name_plural="گروه محصولات"
        
    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    productgroupId = models.ForeignKey(ProductGroup, default=1, on_delete=models.CASCADE, related_name="product_group")
    productSize = models.CharField(max_length=255, blank=True, null=True, verbose_name="سایز کالا")
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_createdby", verbose_name="ایجاد شده توسط")
    isActive = models.BooleanField(default=True, verbose_name="آیا محصول فعال باشد؟")
    isStock = models.BooleanField(default=True, verbose_name="آیا محصول موجود می باشد؟")
    isDeleted = models.BooleanField(default=False, verbose_name="آیا محصول در لیست حذف شده ها باشد؟")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta: 
        db_table = "products"
        verbose_name="محصول"
        verbose_name_plural="محصولات"

    def __str__(self) -> str:
        return self.title

class ProductPrice(models.Model):
    productId = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="شناسه کالا")
    price = models.CharField(max_length=255, blank=True, null=True, verbose_name="قیمت کالا")
    isDeleted = models.BooleanField(default=False, verbose_name="آیا محصول در لیست حذف شده ها باشد؟")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)